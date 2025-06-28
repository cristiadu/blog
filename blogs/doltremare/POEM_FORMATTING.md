# Poem Formatting Guide

This guide explains how to use the poem layout and formatting options for your blog posts.

## Using the Poem Layout

To use the poem layout, simply set the layout in your post's front matter:

```yaml
---
layout: poem
title: "Your Poem Title"
date: 2024-01-15
author: "Your Name"
align: center    # Options: center, left, right, justify
size: normal     # Options: small, normal, large
spacing: normal  # Options: compact, normal, spaced
categories:
  - poetry
  - personal
tags:
  - your-tags
---
```

## Formatting Options

### Poem Alignment
Control the alignment of your entire poem using the `align` field in the frontmatter:

```yaml
---
layout: poem
title: "Your Poem"
align: center  # Options: center, left, right, justify
---
```

**Available alignment options:**
- **center** (default): Centers the poem text
- **left**: Left-aligns the poem text  
- **right**: Right-aligns the poem text
- **justify**: Justifies the poem text (full width)

### Font Size
Control the font size of your poem using the `size` field in the frontmatter:

```yaml
---
layout: poem
title: "Your Poem"
size: normal  # Options: small, normal, large
---
```

**Available size options:**
- **small**: Smaller font size (0.8em) for delicate or subtle poems
- **normal** (default): Standard poem font size (0.9em)
- **large**: Larger font size (1.1em) for impactful or dramatic poems

### Line Spacing
Control the line spacing of your poem using the `spacing` field in the frontmatter:

```yaml
---
layout: poem
title: "Your Poem"
spacing: normal  # Options: compact, normal, spaced
---
```

**Available spacing options:**
- **compact**: Tighter line spacing (line-height: 1.2) for dense poems
- **normal** (default): Standard line spacing (line-height: 1.6) 
- **spaced**: Looser line spacing (line-height: 2) for breathing room

### Basic Poem Content
The poem layout automatically provides optimized typography for poetry with preserved line breaks:

```html
Your poem text here
with line breaks preserved
```

### Using Pre-formatted Text
For exact formatting preservation with proper styling:
```html
<pre>
Poema com formatação
    preservada
        exatamente
            como escrito
</pre>
```

### Stanzas and Verses
For more control over spacing between poem sections:
```html
<div class="stanza">
<div class="verse">First verse</div>
<div class="verse">Second verse</div>
<div class="verse">Third verse</div>
</div>
```

## Examples

### Centered Poem (Default)
```yaml
---
layout: poem
title: "Centered Love Poem"
align: center
---
```
```html
<div class="poem">
"O que dizer de ti?

Quero sempre você aqui.

Tu es minha esperança,

Parece criança,

Me abraça e dança."
</div>
```

### Left-aligned Small Poem
```yaml
---
layout: poem
title: "Subtle Verses"
align: left
size: small
spacing: normal
---
```
```html
Pequenos versos
para poemas delicados
que precisam de sutileza.
```

### Right-aligned Large Poem
```yaml
---
layout: poem
title: "Impact Verses"
align: right
size: large
spacing: spaced
---
```
```html
VERSOS GRANDES
PARA MOMENTOS
DE IMPACTO
E INTENSIDADE.
```

### Compact Spacing Example
```yaml
---
layout: poem
title: "Dense Poem"
align: center
size: normal
spacing: compact
---
```
```html
Dense lines
close together
creating intensity
through proximity
of thoughts.
```

### Pre-formatted Poem with Exact Spacing
```html
<pre>
Tssss

tssss

tss...

it's building up.

It always builds up.
</pre>
```

### Stanzas with Custom Spacing
```html
<div class="stanza">
<div class="verse">First stanza, first line</div>
<div class="verse">First stanza, second line</div>
</div>

<div class="stanza">
<div class="verse">Second stanza, first line</div>
<div class="verse">Second stanza, second line</div>
</div>
```

## Benefits

1. **Optimized Typography**: The poem layout uses a smaller, more readable font size (0.9em vs the default larger size)
2. **Flexible Formatting**: You can control alignment, size, and spacing easily with metadata fields
3. **Preserved Formatting**: Line breaks and spacing are preserved as intended
4. **Responsive Design**: The layout adapts to different screen sizes (0.85em on mobile)
5. **Built-in Styling**: The formatting is built into the theme, so it's stable and maintainable
6. **Clean Pre-formatted Text**: The `pre` tag is styled to blend seamlessly with the theme
7. **Consistent System**: All formatting is controlled through frontmatter fields for easy maintenance

## Converting Existing Posts

To convert an existing poem post to use the new layout:

1. Change `layout: single` to `layout: poem` in the front matter
2. Add formatting fields to control appearance:
   - `align` field to control poem alignment (defaults to `center`)
   - `size` field to control font size (defaults to `normal`)
   - `spacing` field to control line spacing (defaults to `normal`)
3. Wrap your poem content in `<div class="poem">` tags or use `<pre>` for exact formatting

## Tips

- Use `<pre>` tags for poems that need exact spacing preservation
- The poem layout automatically provides better typography for poetry
- Use the formatting fields to match the visual presentation to the poem's mood and style:
  - **Small size + compact spacing** for intimate, whispered poems
  - **Large size + spaced** for dramatic, impactful poems
  - **Left align + normal size** for narrative or flowing poems
  - **Center align + normal** for traditional, balanced poems
- The layout is responsive and will look good on all devices
- All formatting is controlled through metadata fields for consistency
