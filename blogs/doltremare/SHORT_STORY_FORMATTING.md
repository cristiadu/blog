# Short Story Formatting Guide

This guide explains how to use the new `short-story` layout and formatting options for longer prose texts, stories, and narrative content.

## Using the Short Story Layout

To use the short-story layout, set the layout in your post's front matter:

```yaml
---
layout: short-story
title: "Your Story Title"
subtitle: "Optional subtitle or story series information"
date: 2024-01-15
author: "Your Name"
font_size: normal     # Options: small, normal, large
line_height: normal   # Options: compact, normal, spaced
toc: true            # Enable table of contents for chapters
toc_label: "Chapters" # Custom TOC label
epigraph: "Optional quote or epigraph text"
epigraph_source: "— Source of the epigraph"
author_note: "Optional author's note at the end"
categories:
  - fiction
  - short-stories
tags:
  - your-tags
---
```

## Key Features

### 1. Chapter Support with Table of Contents
Enable a table of contents to help readers navigate through chapters:

```yaml
---
layout: short-story
title: "The Long Journey"
toc: true
toc_label: "Chapters"  # Default: "Chapters"
toc_icon: "book-open"  # Default: "book-open"
toc_sticky: true       # Makes TOC stick when scrolling
---

# Chapter 1: The Beginning

Your first chapter content here...

# Chapter 2: The Middle

Your second chapter content here...

# Chapter 3: The End

Your final chapter content here...
```

### 2. Typography Options
Control the typography of your story for optimal reading:

```yaml
---
layout: short-story
title: "Your Story"
font_size: normal     # Options: small, normal, large
line_height: normal   # Options: compact, normal, spaced
---
```

**Font Size Options:**
- **small**: Smaller font for delicate or intimate stories
- **normal** (default): Standard reading font size
- **large**: Larger font for emphasis or accessibility

**Line Height Options:**
- **compact**: Tighter line spacing for dense narratives
- **normal** (default): Comfortable reading line spacing
- **spaced**: Looser spacing for contemplative pieces

### 3. Epigraph Support
Add quotes or epigraphs at the beginning of your story:

```yaml
---
layout: short-story
title: "Reflections"
epigraph: "In the end, we will remember not the words of our enemies, but the silence of our friends."
epigraph_source: "— Martin Luther King Jr."
---
```

### 4. Author's Note
Add personal notes or context at the end of your story:

```yaml
---
layout: short-story
title: "Based on True Events"
author_note: "This story was inspired by events that occurred during my travels in 2019. While the characters are fictional, the emotions and places are very real to me."
---
```

### 5. Subtitle Support
Add subtitles for story series or additional context:

```yaml
---
layout: short-story
title: "The Detective's Dilemma"
subtitle: "A Sarah Chen Mystery, Part 1"
---
```

## Content Formatting

### Chapter Headers
Use standard Markdown headers to create chapters:

```markdown
# Chapter 1: The Discovery

The morning started like any other...

## Section 1.1: The Letter

But when she opened the envelope...

# Chapter 2: The Investigation

Three days later...
```

### Multiple Stories in One Post
You can include multiple related short stories:

```markdown
---
layout: short-story
title: "Three Tales of the City"
toc: true
---

# Story One: The Vendor

Maria had been selling flowers on the corner for twenty years...

---

# Story Two: The Commuter

Every morning at 8:15, James walked past the flower vendor...

---

# Story Three: The Connection

It wasn't until the rainy Tuesday that their worlds collided...
```

### Dialogue and Formatting
The layout preserves standard prose formatting:

```markdown
"I don't understand," Sarah said, her voice barely above a whisper.

Marcus looked up from his newspaper. "What's to understand? It's simple economics."

She shook her head. The numbers on the page blurred together as tears welled in her eyes. How had they gotten to this point?
```

## Complete Example

```yaml
---
layout: short-story
title: "The Last Letter"
subtitle: "A story of forgiveness"
date: 2024-03-15
font_size: normal
line_height: normal
toc: true
toc_label: "Sections"
epigraph: "Forgiveness is not about forgetting. It is about letting go of another person's throat."
epigraph_source: "— William Paul Young"
author_note: "This story explores themes close to my heart. It's dedicated to anyone who has struggled with forgiveness."
categories:
  - fiction
  - drama
tags:
  - forgiveness
  - family
  - letters
---

# The Discovery

Elena found the letter while cleaning out her grandmother's attic...

# The Reading

With trembling hands, she unfolded the yellowed paper...

# The Decision

Three weeks passed before Elena could bring herself to respond...
```

## Tips for Best Results

1. **Use Headers Strategically**: H1 headers create main chapters, H2-H6 for subsections
2. **Enable TOC for Long Stories**: Stories over 1000 words benefit from navigation
3. **Consider Line Height**: Longer stories often read better with normal or spaced line height
4. **Use Horizontal Rules**: Add `---` between distinct sections or stories
5. **Test Typography**: Preview your story with different font sizes to find what works best

## Differences from Poem Layout

- **Text Alignment**: Always left-aligned for optimal prose reading
- **Typography**: Optimized for paragraph text rather than verse
- **Navigation**: Enhanced chapter support with table of contents
- **Additional Features**: Epigraphs, author notes, and subtitles
- **Content Structure**: Designed for flowing narrative rather than structured verse

## Converting from Single Layout

If you have existing stories using the `single` layout, simply change:

```yaml
# Old
layout: single

# New  
layout: short-story
```

The short-story layout includes all the features of the single layout plus the story-specific enhancements described above. 