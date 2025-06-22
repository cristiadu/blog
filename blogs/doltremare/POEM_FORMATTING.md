# Poem Formatting Guide

This guide explains how to use the new poem layout and formatting options for your blog posts.

## Using the Poem Layout

To use the poem layout, simply set the layout in your post's front matter:

```yaml
---
layout: poem
title: "Your Poem Title"
date: 2024-01-15
---
```

## Formatting Options

### Basic Poem (Centered)
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
- **Small**: `class="poem poem-small"`
- **Normal** (default): `class="poem"`
- **Large**: `class="poem poem-large"`

### Spacing Options
- **Spaced** (more line height): `class="poem poem-spaced"`
- **Compact** (less line height): `class="poem poem-compact"`
- **Normal** (default): `class="poem"`

### Combining Options
You can combine multiple options:
```html
<div class="poem poem-left poem-small poem-spaced">
Your poem with multiple formatting options
</div>
```

### Using Pre-formatted Text
For exact formatting preservation:
```html
<pre>
Poema com formatação
    preservada
        exatamente
            como escrito
</pre>
```

### Stanzas and Verses
For more control over spacing:
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

## Benefits

1. **Smaller Font Size**: The poem layout uses a smaller, more readable font size (0.9em vs the default larger size)
2. **Flexible Formatting**: You can now control alignment, size, and spacing for each poem
3. **Preserved Formatting**: Line breaks and spacing are preserved as intended
4. **Responsive**: The layout adapts to different screen sizes
5. **No CSS Overrides**: The formatting is built into the theme, so it's stable and maintainable

## Converting Existing Posts

To convert an existing poem post to use the new layout:

1. Change `layout: single` to `layout: poem` in the front matter
2. Wrap your poem content in `<div class="poem">` tags
3. Add any additional formatting classes as needed

## Tips

- Use the example post (`2024-01-15-example-poem-formatting.md`) as a reference
- Experiment with different combinations of formatting options
- The `pre` tag is useful for poems that need exact spacing preservation
- Consider the emotional impact of different formatting choices for your poems 