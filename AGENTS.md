# AGENTS.md

Guide for AI agents working in this repository.

## What this repo is

One GitHub Pages site (`blog.cristianofaustino.me`) built from **three independent Jekyll
sites** that are stitched together at build time:

| Site | Source | URL | Theme | Post layout(s) |
| --- | --- | --- | --- | --- |
| Hub | `/` (root) | `/` | `abhinavs/moonwalk` (remote) | `post` |
| Coding | `blogs/coding/` | `/coding` | `jekyll-theme-console` | `post` |
| Doltremare | `blogs/doltremare/` | `/doltremare` | `mmistakes/minimal-mistakes@4.16.6` (remote) | `poem`, `short-story` |

Each has its own `_config.yml`, `Gemfile`, `_layouts/`, `_includes/`, `assets/` and `_posts/`.
The root `_config.yml` **excludes `blogs/`**, so the sub-blogs never build as part of the hub —
the `Makefile` builds each one separately into `_site/<name>/`.

Because of this, a change to a sub-blog's theme, layout, or config affects only that sub-blog.
There is no shared layout or include across the three sites; do not try to factor one out.

## Commands

Always go through the `Makefile` — it is the entrypoint for every build task.

```bash
make all          # build hub + all sub-blogs into _site/
make main         # build the hub only
make subblogs     # build every blog under blogs/*/ into _site/<name>/
make update-deps  # bundle update for the hub and every sub-blog
make clean        # rm -rf _site/
```

Ruby version comes from `.ruby-version`. Dependencies are shared through `Gemfile.base`
(`eval_gemfile`), which pulls in the `github-pages` gem so local builds match GitHub Pages —
that gem caps Ruby below 4.0.

Build in a UTF-8 locale; the Minimal Mistakes Sass fails without one.

## Post conventions

Filenames are always `_posts/YYYY-MM-DD-slug.md`, ASCII, accents stripped
(e.g. `2009-11-03-ao-dio-s-dio.md`). Front matter `date` is the source of truth for ordering.

**Hub** (`_posts/`) — `layout: post`, `title`, `author`, `tags`. Dates look like
`2023-07-26 22:49:56 +0000`.

**Coding** (`blogs/coding/_posts/`) — `layout: post`, `title`, `date`, `blog: coding`. Bodies may
contain Liquid tags (`{% highlight ruby %}`); never run these through a WYSIWYG editor.

**Doltremare** (`blogs/doltremare/_posts/`) — 219 posts, two shapes:

- `layout: poem` (218 posts): `title`, `date` (ISO 8601 with offset), `author`,
  `last_modified_at`, `align`, `size`, `spacing`, `categories`, `tags`.
- `layout: short-story` (1 post): `title`, `subtitle`, `date`, `font_size`, `text_spacing`,
  `toc`, `toc_label`, `toc_icon`, `toc_sticky`, `epigraph`, `epigraph_source`, `author_note`,
  `categories`, `tags`.

Keep the key order above — it is what the archive already uses, and matching it keeps diffs
small. Every option is documented in `blogs/doltremare/POEM_FORMATTING.md` and
`blogs/doltremare/SHORT_STORY_FORMATTING.md`; read those before touching a poem or story.

`author` is a key into `blogs/doltremare/_data/authors.yml`, not free text. Minimal Mistakes
looks the author up there to render the sidebar profile.

Poem and short-story bodies carry hand-written HTML (`<pre>`, `<div class="poem">`,
`<div class="dialogue">`) and depend on exact line breaks. Preserve them verbatim.

## Editing posts through the browser

`admin/` serves a Git-based content editor at `https://blog.cristianofaustino.me/admin/`,
configured in Decap CMS format (`admin/config.yml`) with one collection per blog. It runs
[Sveltia CMS](https://sveltiacms.app/) rather than Decap CMS itself because Sveltia can sign in
with a GitHub personal access token, while Decap's GitHub backend requires an OAuth token
exchange running on a server somewhere.

`publish_mode: editorial_workflow` means saving never touches `main`: each entry gets a
`cms/<collection>/<slug>` branch and a pull request, and publishing merges it.

When changing `admin/config.yml`, validate it against the schema referenced on its first line.
The CMS script in `admin/index.html` is pinned to an exact version with an SRI hash; the comment
in that file has the command to recompute the hash on upgrade.

Field definitions must cover **every** front matter key a collection's posts already use.
An undeclared key can be dropped when the CMS rewrites an entry.

## CI/CD

- `.github/workflows/ci.yaml` — runs `make all` on pull requests to `main`; also `workflow_call`.
- `.github/workflows/cd.yml` — calls the CI workflow on push to `main`, then deploys `_site/`
  to GitHub Pages.

Third-party actions are pinned to commit SHAs with the version in a trailing comment. Keep it
that way when adding or bumping an action.

## Known rough edges

- `authors.yml` has no `Monah` entry, but 5 poems use `author: Monah`.
- Two poems use `author: "Bruno  Vinícius"` (double space) instead of `Bruno Vinícius`.
- `_posts/2020-07-07-overview-post.md` (hub) and `blogs/coding/_posts/2023-07-26-welcome-to-jekyll.md`
  are still the theme/Jekyll sample posts.
