# Multi-Blog Jekyll Project

My personal multi-blog Jekyll setup featuring a main blog and many sub-blogs, each with different themes and purposes.

## 📁 Project Structure

```
blog/
├── _config.yml                 # Main blog configuration
├── _posts/                     # Main blog posts
├── admin/                      # Browser-based content editor (see below)
│   ├── index.html
│   └── config.yml
├── _layouts/                   # Main blog layouts
├── _includes/                  # Main blog includes
├── _sass/                      # Main blog styles
├── assets/                     # Main blog assets
├── blogs/
│   ├── coding/                 # Coding blog (Console theme)
│   │   ├── _config.yml
│   │   ├── _posts/
│   │   ├── _layouts/
│   │   ├── _includes/
│   │   ├── assets/
│   │   └── Gemfile
│   └── doltremare/            # Creative writing blog (Minimal Mistakes theme)
│       ├── _config.yml
│       ├── _posts/
│       ├── _layouts/
│       ├── _includes/
│       ├── assets/
│       └── Gemfile
├── Gemfile.base               # Shared dependencies
├── Gemfile                    # Main blog dependencies
├── Makefile                   # Build automation
├── AGENTS.md                  # Repository guide for AI agents
└── README.md                  # README for the project
```

## 🎨 Blog Themes

- **Main Blog**: Custom theme with dark/light mode support
- **Coding Blog**: Console theme with hacker/dark/light variants
- **Doltremare Blog**: Minimal Mistakes theme with sunrise skin

## 🚀 Quick Start

### Prerequisites

- Ruby as pinned in `.ruby-version` (managed via rbenv)
- Bundler
- Make

### Installation

The project uses a Makefile for automation:

```bash
# Install all dependencies and Build all blogs
make all
```

## 📝 Blog Configuration

### Main Blog
- **URL**: `https://blog.cristianofaustino.me`
- **Theme**: Custom theme with toggle-able dark/light modes
- **Usage**: Main Hub for the other blogs + general info.

### Coding Blog
- **URL**: `https://blog.cristianofaustino.me/coding`
- **Theme**: Console theme with multiple color schemes
- **Usage**: Coding articles.

### Doltremare Blog
- **URL**: `https://blog.cristianofaustino.me/doltremare`
- **Theme**: Minimal Mistakes with sunrise skin.
- **Usage**: Creative writing focus, sharing my writing.

## 🔧 Development

### Adding New Posts

- **Main blog**: Add files to `_posts/`
- **Coding blog**: Add files to `blogs/coding/_posts/`
- **Doltremare blog**: Add files to `blogs/doltremare/_posts/`

Or edit them in the browser at
[blog.cristianofaustino.me/admin](https://blog.cristianofaustino.me/admin/) — see
[Editing Posts in the Browser](#-editing-posts-in-the-browser).

## ✏️ Editing Posts in the Browser

`admin/` serves a Git-based content editor at
[blog.cristianofaustino.me/admin](https://blog.cristianofaustino.me/admin/), with one collection
per blog. It is configured in [Decap CMS](https://decapcms.org/docs/jekyll/) format
(`admin/config.yml`) and runs [Sveltia CMS](https://sveltiacms.app/), a drop-in replacement that
can sign in with a GitHub token instead of needing a hosted OAuth service.

### Signing in

1. Open [/admin/](https://blog.cristianofaustino.me/admin/) and click **Sign In with Token**.
2. Follow the link in the dialog to create a GitHub personal access token (the required scopes
   are pre-selected) and paste it back.

The token stays in that browser's local storage and is never committed. Create it as a
fine-grained token limited to `cristiadu/blog` with read/write access to *Contents* and
*Pull requests*, and re-issue it when it expires.

### Saving and publishing

Saving never writes to `main`. Each entry lives on a `cms/<collection>/<slug>` branch with an
open pull request, so writing and releasing are separate steps:

| In the editor | In the repository |
| --- | --- |
| Save a new entry | Branch created, entry committed, pull request opened as a draft |
| Save again | Another commit on the same branch |
| Send for review / mark ready | Pull request label updated, draft flag cleared |
| **Publish** | Pull request merged (squashed) and branch deleted |
| Discard | Pull request closed without merging, branch deleted |

The `[CI] Build all Blogs` workflow builds every pull request, so a post that breaks the build
shows up as a failed check before it is published. Merging to `main` triggers the deploy.

## 🚀 Deployment

### GitHub Pages

The project is configured for GitHub Pages deployment:
- Uses `github-pages` gem for compatibility
- Remote themes for sub-blogs
- Automatic builds via GitHub Actions

### Manual Deployment

1. Build the site:
   ```bash
   make all
   ```

2. Deploy the `_site/` directory to your web server

---

**_Built with ❤️ using Jekyll_**
