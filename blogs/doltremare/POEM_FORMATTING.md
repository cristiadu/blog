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
categories:
  - poetry
  - personal
tags:
  - your-tags
---
```

## Formatting Options

### Basic Poem (Centered)
The poem layout automatically provides a smaller, more readable font size (0.9em) and better line spacing for poetry:

```html
<div class="poem">
Your poem text here
with line breaks preserved
</div>
```

### Alignment Options
- **Left-aligned**: `class="poem poem-left"`
- **Right-aligned**: `class="poem poem-right"`
- **Justified**: `class="poem poem-justify"`
- **Centered** (default): `class="poem"`

### Font Size Options
- **Small**: `class="poem poem-small"` (0.8em)
- **Normal** (default): `class="poem"` (0.9em)
- **Large**: `class="poem poem-large"` (1.1em)

### Spacing Options
- **Spaced** (more line height): `class="poem poem-spaced"` (line-height: 2)
- **Compact** (less line height): `class="poem poem-compact"` (line-height: 1.2)
- **Normal** (default): `class="poem"` (line-height: 1.6)

### Combining Options
You can combine multiple options:
```html
<div class="poem poem-left poem-small poem-spaced">
Your poem with multiple formatting options
</div>
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

### Simple Centered Poem
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
```html
<div class="poem poem-left poem-small">
Pequenos versos
em fonte menor
para poemas delicados
que precisam de sutileza.
</div>
```

### Right-aligned Large Poem
```html
<div class="poem poem-right poem-large">
VERSOS GRANDES
PARA MOMENTOS
DE IMPACTO
E INTENSIDADE.
</div>
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
2. **Flexible Formatting**: You can control alignment, size, and spacing for each poem
3. **Preserved Formatting**: Line breaks and spacing are preserved as intended
4. **Responsive Design**: The layout adapts to different screen sizes (0.85em on mobile)
5. **Built-in Styling**: The formatting is built into the theme, so it's stable and maintainable
6. **Clean Pre-formatted Text**: The `pre` tag is styled to blend seamlessly with the theme

## Converting Existing Posts

To convert an existing poem post to use the new layout:

1. Change `layout: single` to `layout: poem` in the front matter
2. Wrap your poem content in `<div class="poem">` tags or use `<pre>` for exact formatting
3. Add any additional formatting classes as needed

## Tips

- Use `<pre>` tags for poems that need exact spacing preservation
- The poem layout automatically provides better typography for poetry
- Experiment with different combinations of formatting options
- Consider the emotional impact of different formatting choices for your poems
- The layout is responsive and will look good on all devices
- You can mix different formatting approaches within the same post
