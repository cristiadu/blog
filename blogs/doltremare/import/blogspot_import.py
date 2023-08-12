import os
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Input XML file containing Blogspot export
INPUT_XML = "data/blogspot.xml"

# Output directory for converted posts
OUTPUT_DIR = "data/posts"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

            # Clean up content using BeautifulSoup
            soup = BeautifulSoup(content, "html.parser")
            cleaned_content = str(soup)

            # Convert HTML formatting to Markdown
            cleaned_content = cleaned_content.replace("<h1>", "# ")
            cleaned_content = cleaned_content.replace("<h1>", "# ")
            cleaned_content = cleaned_content.replace("<h2>", "## ")
            cleaned_content = cleaned_content.replace("<h3>", "### ")
            cleaned_content = cleaned_content.replace("<h4>", "#### ")
            cleaned_content = cleaned_content.replace("<h5>", "##### ")
            cleaned_content = cleaned_content.replace("<h6>", "###### ")
            cleaned_content = cleaned_content.replace("<strong>", "**")
            cleaned_content = cleaned_content.replace("</strong>", "**")
            cleaned_content = cleaned_content.replace("<b>", "**")
            cleaned_content = cleaned_content.replace("</b>", "**")
            cleaned_content = cleaned_content.replace('<span style="font-weight: bold;">', "")
            cleaned_content = cleaned_content.replace('<span style="font-style: italic;">', "")
            cleaned_content = cleaned_content.replace('<span style="font-style:italic;">', "")
            cleaned_content = cleaned_content.replace("<span>", "")
            cleaned_content = cleaned_content.replace("</span>", "")
            cleaned_content = cleaned_content.replace('<span style="font-style: italic;">', "")
            cleaned_content = cleaned_content.replace("</span>", "")
            cleaned_content = cleaned_content.replace("<em>", "*")
            cleaned_content = cleaned_content.replace("</em>", "*")
            cleaned_content = cleaned_content.replace("<i>", "*")
            cleaned_content = cleaned_content.replace("</i>", "*")
            cleaned_content = cleaned_content.replace("<ul>", "")
            cleaned_content = cleaned_content.replace("</ul>", "")
            cleaned_content = cleaned_content.replace("<li>", "- ")
            cleaned_content = cleaned_content.replace("</li>", "\n")
            cleaned_content = cleaned_content.replace('<div class="MsoNormal">', "")       
            cleaned_content = cleaned_content.replace('<div style="text-align: left;">', "")
            cleaned_content = cleaned_content.replace('<div style="text-align: center;">', "")       
            cleaned_content = cleaned_content.replace("<div>", "")
            cleaned_content = cleaned_content.replace("</div>", "\n")
            cleaned_content = cleaned_content.replace("<p>", "")
            cleaned_content = cleaned_content.replace('<p style="text-align: center;">', "")
            cleaned_content = cleaned_content.replace("</p>", "\n")
            cleaned_content = cleaned_content.replace("<br>", "\n")
            cleaned_content = cleaned_content.replace("<br/>", "\n")
            cleaned_content = cleaned_content.replace("<blockquote>", "> ")
            cleaned_content = cleaned_content.replace("</blockquote>", "\n")

            # Create Minimal Mistakes post front matter
            front_matter = f"""
---
layout: single
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
