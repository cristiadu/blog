# Multi-Blog Jekyll Project

My personal multi-blog Jekyll setup featuring a main blog and many sub-blogs, each with different themes and purposes.

## 📁 Project Structure

```
blog/
├── _config.yml                 # Main blog configuration
├── _posts/                     # Main blog posts
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
└── README.md                  # README for the project
```

## 🎨 Blog Themes

- **Main Blog**: Custom theme with dark/light mode support
- **Coding Blog**: Console theme with hacker/dark/light variants
- **Doltremare Blog**: Minimal Mistakes theme with sunrise skin

## 🚀 Quick Start

### Prerequisites

- Ruby 3.2.2 (managed via rbenv)
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
