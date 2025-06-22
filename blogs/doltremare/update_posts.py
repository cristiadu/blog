#!/usr/bin/env python3
"""
Script to update all doltremare posts to use the poem layout and preserve meaningful HTML formatting.
"""

import os
import re
from pathlib import Path

def clean_html_content(content):
    """Convert HTML formatting to equivalent markdown while preserving meaningful structure."""
    # Convert <br> tags to newlines
    content = re.sub(r'<br\s*/?>', '\n', content)
    
    # Convert <div> tags to newlines (for stanza breaks)
    content = re.sub(r'<div[^>]*>', '', content)
    content = re.sub(r'</div>', '\n', content)
    
    # Convert <a> tags to markdown links
    content = re.sub(r'<a\s+href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', content)
    
    # Convert <b> and <strong> to markdown bold
    content = re.sub(r'<(b|strong)[^>]*>', '**', content)
    content = re.sub(r'</(b|strong)>', '**', content)
    
    # Convert <i> and <em> to markdown italic
    content = re.sub(r'<(i|em)[^>]*>', '*', content)
    content = re.sub(r'</(i|em)>', '*', content)
    
    # Remove only HTML tags that don't have meaningful formatting
    # But preserve span and other meaningful tags
    content = re.sub(r'<(?!span\b)[^>]+>', '', content)
    
    # Clean up multiple line breaks
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

def format_poem_content(content):
    """Format content by converting HTML to markdown and preserving stanza breaks."""
    content = clean_html_content(content)
    # Remove excessive leading/trailing blank lines
    content = content.strip('\n')
    return content

def update_post_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it already has poem layout
    has_poem_layout = 'layout: poem' in content
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            post_content = parts[2]
        else:
            print(f"Error parsing {file_path.name}")
            return False
    else:
        print(f"Error: {file_path.name} doesn't have proper front matter")
        return False
    
    # Update front matter to use poem layout if not already
    if not has_poem_layout:
        front_matter = re.sub(r'layout:\s*single', 'layout: poem', front_matter)
    
    # Format the content (this will convert HTML to markdown)
    formatted_content = format_poem_content(post_content)
    
    new_content = f"---{front_matter}---\n\n{formatted_content}\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    if has_poem_layout:
        print(f"Cleaned up {file_path.name}")
    else:
        print(f"Updated {file_path.name}")
    return True

def main():
    posts_dir = Path('_posts')
    if not posts_dir.exists():
        print("Error: _posts directory not found")
        return
    updated_count = 0
    total_count = 0
    for file_path in posts_dir.glob('*.md'):
        if file_path.name == '2024-01-15-example-poem-formatting.md':
            continue
        total_count += 1
        if update_post_file(file_path):
            updated_count += 1
    print(f"\nProcessing complete!")
    print(f"Total files processed: {total_count}")
    print(f"Files updated: {updated_count}")

if __name__ == '__main__':
    main() 