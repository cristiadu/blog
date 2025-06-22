import os
import re
import xml.etree.ElementTree as ET
import html

# Input XML file containing Blogspot export
INPUT_XML = "data/blogspot.xml"

# Output directory for converted posts
OUTPUT_DIR = "../_posts"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_html_content(content):
    """Convert escaped HTML formatting to equivalent markdown while preserving meaningful structure."""
    # First, unescape the HTML entities
    content = html.unescape(content)
    
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
    
    # Convert <blockquote> to markdown blockquotes
    content = re.sub(r'<blockquote[^>]*>', '> ', content)
    content = re.sub(r'</blockquote>', '\n\n', content)
    
    # Remove only HTML tags that don't have meaningful formatting
    # But preserve span and other meaningful tags
    content = re.sub(r'<(?!span\b)[^>]+>', '', content)
    
    # Clean up multiple line breaks
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()

# Parse the XML file
tree = ET.parse(INPUT_XML)
root = tree.getroot()

# Iterate through each <entry> element in the XML
for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
    content_type = entry.find("{http://www.w3.org/2005/Atom}content").get("type") if entry.find("{http://www.w3.org/2005/Atom}content") is not None else 'none'
    
    # Process only the post entries
    if content_type == "html":
        author = entry.find("{http://www.w3.org/2005/Atom}author").find("{http://www.w3.org/2005/Atom}name").text
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        category = entry.find("{http://www.w3.org/2005/Atom}category").get("term")

        if author != 'Thomas Domingues' and title is not None and category != "http://schemas.google.com/blogger/2008/kind#comment":
            content = entry.find("{http://www.w3.org/2005/Atom}content").text
            published = entry.find("{http://www.w3.org/2005/Atom}published").text
            updated = entry.find("{http://www.w3.org/2005/Atom}updated").text

            # Clean up content using our custom function
            cleaned_content = clean_html_content(content)

            # Create poem post front matter
            front_matter = f"""---
layout: poem
title: "{title}"
date: {published}
author: "{author}"
last_modified_at: {updated}
categories:
  - imported
  - blogspot
tags:
  - blogspot
  - "{author}"
---
"""

            # Combine front matter and cleaned content
            formatted_content = front_matter + "\n" + cleaned_content

            # Generate a filename based on the title
            filename = published[:10] + "-" + re.sub(r'\s+', '-', title.lower().replace('/','')) + ".md"
            output_file_path = os.path.join(OUTPUT_DIR, filename)

            # Write the formatted content to the output file
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.write(formatted_content)

            print(f"Converted '{title}' and saved to {output_file_path}")

print("Processing complete!")
