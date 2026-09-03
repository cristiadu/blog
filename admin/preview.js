/*
  Preview templates for the content editor.

  Every collection is previewed with the stylesheets and the layout markup of the blog
  it belongs to, so the preview pane matches the built page. Site chrome — mastheads,
  menus, footers, related posts — is left out; only the post itself is rendered.

  Sveltia CMS builds the preview pane as an iframe whose <head> holds nothing but the
  styles registered for it, which is why each template swaps the <link> elements
  instead of registering all three themes at once: loaded together they would style
  each other.
*/
(() => {
  const { CMS, createClass, h, rf } = window;

  // Mirrors the <head> of each blog's layout: the hub's main.css, the console theme
  // variant selected by `style: dark`, and Minimal Mistakes plus the per-layout CSS
  // from blogs/doltremare/_includes/head/custom.html.
  const STYLESHEETS = {
    hub: ['/assets/css/main.css'],
    coding: ['/coding/assets/main-dark.css'],
    doltremare: [
      '/doltremare/assets/css/main.css',
      '/doltremare/assets/css/posts.css',
      '/doltremare/assets/css/poem.css',
      '/doltremare/assets/css/short-story.css',
    ],
  };

  // The hub reads its palette from html[data-theme]; the other two blogs ignore it.
  const HTML_THEMES = { hub: 'dark' };

  const LONG_DATE = { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' };
  const MONTH_AND_YEAR = { year: 'numeric', month: 'long', timeZone: 'UTC' };

  const applyBlogChrome = (doc, blog, bodyClass = '') => {
    const hrefs = STYLESHEETS[blog];

    doc.head.querySelectorAll('link[data-blog-css]').forEach((link) => {
      if (!hrefs.includes(link.getAttribute('href'))) {
        link.remove();
      }
    });

    hrefs
      .filter((href) => !doc.head.querySelector(`link[data-blog-css][href="${href}"]`))
      .forEach((href) => {
        const link = doc.createElement('link');

        link.rel = 'stylesheet';
        link.setAttribute('href', href);
        link.dataset.blogCss = '';
        doc.head.append(link);
      });

    const theme = HTML_THEMES[blog];

    if (theme) {
      doc.documentElement.dataset.theme = theme;
    } else {
      delete doc.documentElement.dataset.theme;
    }

    doc.body.className = bodyClass;
  };

  // Formatted from the date part alone, so the entry's UTC offset cannot shift the day.
  const formatDate = (value, options) => {
    const parts = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(value ?? ''));

    if (!parts) {
      return '';
    }

    const day = new Date(Date.UTC(Number(parts[1]), Number(parts[2]) - 1, Number(parts[3])));

    return new Intl.DateTimeFormat('en-US', options).format(day);
  };

  const countWords = (body) =>
    String(body ?? '')
      .replace(/<[^>]*>/g, ' ')
      .split(/\s+/)
      .filter(Boolean).length;

  const values = (entry) => entry.get('data')?.toJS() ?? {};

  const listOf = (value) => (Array.isArray(value) ? value.filter(Boolean) : []);

  const classList = (...names) => names.filter(Boolean).join(' ');

  /* ---------------------------------------------------------------- hub (moonwalk) */

  // _includes/date_and_social_share.html prints the word count less one minute's worth
  // of words, and hides the whole reading time for posts under 180 words.
  const hubReadingTime = (body) => {
    const words = countWords(body);

    return words < 180 ? '' : ` (${words - 180} Words, ${Math.floor(words / 180)} Minutes)`;
  };

  const HubPostPreview = createClass({
    componentDidMount: function () {
      applyBlogChrome(this.props.document, 'hub');
    },
    render: function () {
      const { entry, widgetFor } = this.props;
      const data = values(entry);
      const tags = listOf(data.tags);

      return h(
        'main',
        { className: 'page-content' },
        h(
          'div',
          { className: 'w' },
          h('a', { href: '/' }, 'home..'),
          h('h1', { className: 'post-title' }, data.title),
          h(
            'p',
            { className: 'post-date text-bold' },
            data.author ? h('span', { className: 'text-upcase' }, data.author) : null,
            data.author ? ' / ' : null,
            h('span', { className: 'text-upcase' }, formatDate(data.date, MONTH_AND_YEAR)),
            hubReadingTime(data.body),
          ),
          tags.length
            ? h(
                'div',
                {},
                tags.map((tag) => h('span', { className: 'tag', key: tag }, tag)),
              )
            : null,
          widgetFor('body'),
        ),
      );
    },
  });

  /* ------------------------------------------------------- coding (jekyll-theme-console) */

  const CodingPostPreview = createClass({
    componentDidMount: function () {
      applyBlogChrome(this.props.document, 'coding');
    },
    render: function () {
      // blogs/coding/_layouts/post.html renders the body and nothing else — no title,
      // no date.
      return h('div', { className: 'container' }, h('main', {}, this.props.widgetFor('body')));
    },
  });

  /* --------------------------------------------- doltremare (minimal-mistakes) */

  const readTime = (body) => {
    const minutes = Math.floor(countWords(body) / 200);

    return minutes < 1 ? 'less than 1 minute read' : `${minutes} minute read`;
  };

  const pageTitle = (title) =>
    h('h1', { id: 'page-title', className: 'page__title p-name' }, h('a', { href: '#' }, title));

  const pageMeta = (data) =>
    h(
      'p',
      { className: 'page__meta' },
      h(
        'span',
        { className: 'page__meta-date' },
        h('i', { className: 'far fa-calendar-alt' }),
        ' ',
        h('time', {}, formatDate(data.date, LONG_DATE)),
      ),
      h('span', { className: 'page__meta-sep' }),
      h(
        'span',
        { className: 'page__meta-readtime' },
        h('i', { className: 'far fa-clock' }),
        ' ',
        readTime(data.body),
      ),
    );

  const taxonomyList = (label, icon, items) =>
    items.length
      ? h(
          'p',
          { className: 'page__taxonomy' },
          h('strong', {}, h('i', { className: `fas fa-fw fa-${icon}` }), ` ${label}: `),
          h(
            'span',
            {},
            items.map((item, index) =>
              h(
                rf,
                { key: item },
                index ? h('span', { className: 'sep' }, ', ') : null,
                h('a', { className: 'page__taxonomy-item p-category', rel: 'tag', href: '#' }, item),
              ),
            ),
          ),
        )
      : null;

  const pageDate = (data) =>
    h(
      'p',
      { className: 'page__date' },
      h('strong', {}, h('i', { className: 'fas fa-fw fa-calendar-alt' }), ' Updated:'),
      ' ',
      h('time', { className: 'dt-published' }, formatDate(data.last_modified_at || data.date, LONG_DATE)),
    );

  // Both Doltremare layouts wrap the body in the same skeleton, differing only in the
  // header, the layout name and the content wrapper.
  const doltremarePage = ({ data, layout, header, content }) =>
    h(
      'div',
      { className: 'initial-content' },
      h(
        'div',
        { id: 'main' },
        h('header', {}, header),
        h(
          'article',
          { className: `page h-entry ${layout}-layout` },
          h(
            'div',
            { className: 'page__inner-wrap' },
            h('section', { className: `page__content e-content ${layout}-content` }, content),
            h(
              'footer',
              { className: 'page__meta' },
              taxonomyList('Tags', 'tags', listOf(data.tags)),
              taxonomyList('Categories', 'folder-open', listOf(data.categories)),
              pageDate(data),
            ),
          ),
        ),
      ),
    );

  const PoemPreview = createClass({
    componentDidMount: function () {
      applyBlogChrome(this.props.document, 'doltremare', 'layout--poem');
    },
    render: function () {
      const { entry, widgetFor } = this.props;
      const data = values(entry);

      return doltremarePage({
        data,
        layout: 'poem',
        header: h(rf, {}, pageTitle(data.title), pageMeta(data)),
        content: h(
          'div',
          {
            className: classList(
              'poem',
              data.align && data.align !== 'center' ? `poem-${data.align}` : '',
              data.size && data.size !== 'normal' ? `poem-${data.size}` : '',
              data.spacing && data.spacing !== 'normal' ? `poem-${data.spacing}` : '',
            ),
          },
          widgetFor('body'),
        ),
      });
    },
  });

  // The live TOC is built from the rendered HTML by Minimal Mistakes' toc.html; here the
  // headings come straight from the Markdown, flat rather than nested.
  const tocAside = (data) =>
    h(
      'aside',
      { className: classList('sidebar__right', data.toc_sticky ? 'sticky' : '') },
      h(
        'nav',
        { className: 'toc' },
        h(
          'header',
          {},
          h(
            'h4',
            { className: 'nav__title' },
            h('i', { className: `fas fa-${data.toc_icon || 'book-open'}` }),
            ` ${data.toc_label || 'Chapters'}`,
          ),
        ),
        h(
          'ul',
          { className: 'toc__menu' },
          [...String(data.body ?? '').matchAll(/^#{1,6}[ \t]+(.+?)[ \t]*#*$/gm)].map(([, text], index) =>
            h('li', { key: `${index}-${text}` }, h('a', { href: '#' }, text)),
          ),
        ),
      ),
    );

  const ShortStoryPreview = createClass({
    componentDidMount: function () {
      applyBlogChrome(this.props.document, 'doltremare', 'layout--short-story');
    },
    render: function () {
      const { entry, widgetFor } = this.props;
      const data = values(entry);

      return doltremarePage({
        data,
        layout: 'short-story',
        header: h(
          rf,
          {},
          pageTitle(data.title),
          data.subtitle ? h('h2', { className: 'page__subtitle' }, data.subtitle) : null,
          pageMeta(data),
        ),
        content: h(
          rf,
          {},
          data.toc ? tocAside(data) : null,
          h(
            'div',
            {
              className: classList(
                'short-story',
                data.font_size && data.font_size !== 'normal' ? `short-story-${data.font_size}` : '',
                data.text_spacing && data.text_spacing !== 'normal'
                  ? `short-story-text-spacing-${data.text_spacing}`
                  : '',
              ),
            },
            data.epigraph
              ? h(
                  'div',
                  { className: 'short-story__epigraph' },
                  h(
                    'blockquote',
                    {},
                    h('p', {}, data.epigraph),
                    data.epigraph_source ? h('cite', {}, data.epigraph_source) : null,
                  ),
                )
              : null,
            widgetFor('body'),
            data.author_note
              ? h(
                  'div',
                  { className: 'short-story__author-note' },
                  h('hr', {}),
                  h('p', {}, h('strong', {}, "Author's Note:"), ` ${data.author_note}`),
                )
              : null,
          ),
        ),
      });
    },
  });

  CMS.registerPreviewTemplate('hub', HubPostPreview);
  CMS.registerPreviewTemplate('coding', CodingPostPreview);
  CMS.registerPreviewTemplate('doltremare_poems', PoemPreview);
  CMS.registerPreviewTemplate('doltremare_stories', ShortStoryPreview);
})();
