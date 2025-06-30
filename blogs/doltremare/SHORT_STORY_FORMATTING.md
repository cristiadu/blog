# Short Story Formatting Guide

The `short-story` layout is designed for longer prose texts with chapter support and enhanced dialogue formatting.

## Front Matter Options

```yaml
---
layout: short-story
title: "Your Story Title"
subtitle: "Optional subtitle"               # Story series info
date: 2024-01-15
font_size: normal                          # small, normal, large
text_spacing: normal                       # compact, normal, spaced
toc: true                                  # Enable table of contents
toc_label: "Chapters"                      # Custom TOC label
toc_icon: "book-open"                      # FontAwesome icon
toc_sticky: true                           # Sticky TOC when scrolling
epigraph: "Quote text"                     # Opening quote
epigraph_source: "— Author Name"           # Quote attribution
author_note: "Author's note text"          # End note
categories: [fiction, short-stories]
tags: [your-tags]
---
```

## Chapter Navigation

Use `#` for chapters, `##` for sections. TOC auto-generates from all headers and appears as sticky sidebar.

## Dialogue Formatting Options

### Basic Dialogue
```html
<div class="dialogue">
  <span class="speaker">Name:</span>
  <span class="speech">"Dialogue text"</span>
</div>
```

### Enhanced Dialogue with Colors
```html
<div class="dialogue-emphasized dialogue-red">
  <span class="speaker">Character</span>
  <span class="speech">"Dialogue text"</span>
</div>
```

**Available Colors:** `dialogue-red`, `dialogue-green`, `dialogue-blue`, `dialogue-purple`, `dialogue-orange`, `dialogue-teal`, `dialogue-pink`

### Special Dialogue Effects

**Whispered Dialogue**
```html
<span class="speech whisper">"Whispered text"</span>
```

**Shouted Dialogue**
```html
<span class="speech shout">"Shouted text"</span>
```

**Distant/Phone Dialogue**
```html
<span class="speech distant">"Distant voice"</span>
```

**Internal Thoughts**
```html
<div class="thought">Internal monologue text</div>
```

### Combined Effects
```html
<div class="dialogue-emphasized dialogue-blue">
  <span class="speaker">Character</span>
  <span class="speech whisper">"Quiet, urgent dialogue"</span>
</div>
```

## Table of Contents Options

```yaml
toc: true                    # Enable/disable TOC
toc_label: "Chapters"        # TOC heading text
toc_icon: "book-open"        # FontAwesome icon name
toc_sticky: true             # TOC follows when scrolling
```

**Options:**
- `toc: true/false` - Shows/hides the table of contents sidebar
- `toc_label` - Custom heading for the TOC (default: "Chapters")
- `toc_icon` - Any FontAwesome icon name (default: "book-open")
- `toc_sticky: true/false` - Whether TOC stays visible when scrolling

**Common Icons:** `book-open`, `list`, `file-alt`, `bookmark`, `map`, `compass`

## Typography Options

```yaml
font_size: normal           # small, normal, large
text_spacing: normal        # compact, normal, spaced
```

**Font Size Options:**
- `small` - Smaller text for longer stories
- `normal` - Default size (1.1em)
- `large` - Larger text for easier reading

**Text Spacing Options:**
- `compact` - Tighter line spacing (1.4)
- `normal` - Default spacing (1.7)
- `spaced` - Looser spacing (2.0)

## Subtitle Options

```yaml
subtitle: "Optional subtitle text"    # Story series, part number, etc.
```

Appears below the main title. Use for series info, genre, or context.

## Epigraph Options

```yaml
epigraph: "Your opening quote text"
epigraph_source: "— Author Name"       # Optional attribution
```

Displays as italicized quote before story content. Good for thematic quotes or lyrics.

## Author's Note Options

```yaml
author_note: "Your note to readers"    # Appears at story end
```

Shows in highlighted box at story end. Use for context, inspiration, or dedication.

## Complete Example

```yaml
  ---
  layout: short-story
  title: "The Last Conversation"
  subtitle: "A story of reconciliation"
  date: 2024-01-15
  font_size: normal
  text_spacing: normal
  toc: true
  toc_label: "Chapters"
  toc_icon: "book-open"
  toc_sticky: true
  epigraph: "Sometimes the most important conversations happen when we think it's too late."
  epigraph_source: "— Anonymous"
  author_note: "This story explores themes of forgiveness and second chances."
  categories:
    - fiction
    - drama
  tags:
    - family
    - forgiveness
  ---

  # Chapter 1: The Call

  The phone rang at 3 AM. Sarah knew it couldn't be good news.

  <div class="dialogue-emphasized dialogue-red">
    <span class="speaker">Sarah</span>
    <span class="speech">"Hello?"</span>
  </div>

  <div class="dialogue-emphasized dialogue-blue">
    <span class="speaker">Dr. Martinez</span>
    <span class="speech">"Is this Sarah Chen? I'm calling about your father."</span>
  </div>

  <div class="thought">
  This was the call she'd been dreading for months.
  </div>

  ## Section 1.1: The News

  <div class="dialogue-emphasized dialogue-blue">
    <span class="speaker">Dr. Martinez</span>
    <span class="speech">"He's asking for you. I think... I think you should come soon."</span>
  </div>

  <div class="dialogue-emphasized dialogue-red">
    <span class="speaker">Sarah</span>
    <span class="speech whisper">"How long does he have?"</span>
  </div>

  A crash echoed from somewhere in the hospital, followed by shouting.

  <div class="dialogue">
    <span class="speaker">Nurse:</span>
    <span class="speech shout">"We need help in room 314!"</span>
  </div>

  # Chapter 2: The Journey

  Sarah hadn't spoken to her father in five years. The drive to the hospital felt endless.

  <div class="dialogue-emphasized dialogue-green">
    <span class="speaker">Tom (on phone)</span>
    <span class="speech distant">"Are you sure about this? You don't owe him anything."</span>
  </div>

  <div class="dialogue-emphasized dialogue-red">
    <span class="speaker">Sarah</span>
    <span class="speech">"Maybe not. But I owe myself this conversation."</span>
  </div>

  The connection crackled with static.

  <div class="dialogue">
    <span class="speaker">Tom:</span>
    <span class="speech distant">"Sarah? Can you hear me?"</span>
  </div>

  # Chapter 3: The Hospital

  Her father looked smaller than she remembered, fragile against the white hospital sheets.

  <div class="dialogue-emphasized dialogue-purple">
    <span class="speaker">Father</span>
    <span class="speech whisper">"Sarah? You came."</span>
  </div>

  <div class="dialogue-emphasized dialogue-red">
    <span class="speaker">Sarah</span>
    <span class="speech">"I'm here, Dad."</span>
  </div>

  <div class="dialogue-emphasized dialogue-purple">
    <span class="speaker">Father</span>
    <span class="speech">"I'm sorry. For everything. I should have—"</span>
  </div>

  <div class="dialogue-emphasized dialogue-red">
    <span class="speaker">Sarah</span>
    <span class="speech whisper">"Dad, please. Just rest."</span>
  </div>

  <div class="thought">
  Forgiveness, she realized, wasn't about forgetting. It was about choosing to move forward.
  </div>

  ---

  # Story Two: The Letter

  Sometimes the most important words are the ones we never send...

```
