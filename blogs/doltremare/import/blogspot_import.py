import os
import re
import xml.etree.ElementTree as ET
import html

# Configuration
INPUT_XML = "data/blogspot.xml"
OUTPUT_DIR = "../_posts"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


def img_replacer(match):
    """Replace img tag with markdown image and return the URL for tracking."""
    url = match.group(1)
    return f'![Image Here]({url})\n', url


def remove_microsoft_word_css(content):
    """Remove Microsoft Word/Internet Explorer CSS styling that clutters posts."""
    # Remove multi-line CSS blocks starting with "Normal"
    content = re.sub(
        r'''Normal[^\n]*\n(?:.|\n)*?/\* Style Definitions \*/(?:.|\n)*?\{(?:.|\n)*?\}[ \t\r\f\v]*''',
        '',
        content,
        flags=re.MULTILINE
    )
    
    # Remove single-line variant
    content = re.sub(
        r'Normal\s+\d+\s+\d+\s+false\s+false\s+false.*?MicrosoftInternetExplorer4.*?mso-bidi-language:#0400;\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content


def handle_images_and_links(content):
    """Extract and embed images, handle image links, and convert regular links to markdown."""
    image_links = []
    
    # Handle images wrapped in anchor tags - convert to just the image
    def img_in_link_replacer(match):
        img_url = match.group(1)
        image_links.append(img_url)
        return f'![Image Here]({img_url})\n'
    
    # Convert <a><img src="..."></a> to just the image
    content = re.sub(r'<a[^>]*>\s*<img[^>]*src="([^"]*)"[^>]*>\s*</a>', img_in_link_replacer, content)
    content = re.sub(r'<a[^>]*>\s*<img[^>]*src=\'([^\']*)\'[^>]*>\s*</a>', img_in_link_replacer, content)
    
    # Extract and embed remaining standalone images
    def process_img_match(match):
        markdown_img, url = img_replacer(match)
        image_links.append(url)
        return markdown_img
    
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', process_img_match, content)
    content = re.sub(r'<img[^>]*src=\'([^\']*)\'[^>]*>', process_img_match, content)
    
    # Convert regular <a> tags to markdown links
    content = re.sub(r'<a\s+href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', content)
    
    return content, image_links


def close_tags_properly(content):
    """Close any unclosed <p> tags before opening new ones."""
    # Split content into lines to process tag by tag
    lines = content.split('\n')
    result_lines = []
    open_ps = 0
    
    for line in lines:
        # Count opening and closing tags in this line
        p_opens = len(re.findall(r'<p[^>]*>', line))
        p_closes = len(re.findall(r'</p>', line))
        
        # If we're opening a new p and there's already an open p, close it first
        if p_opens > 0 and open_ps > 0:
            result_lines.append('</p>' * open_ps)
            open_ps = 0
        
        # Add the current line
        result_lines.append(line)
        
        # Update counters
        open_ps += p_opens - p_closes
    
    # Close any remaining open p tags at the end
    if open_ps > 0:
        result_lines.append('</p>' * open_ps)
    
    return '\n'.join(result_lines)


def convert_html_to_markdown(html_content):
    """Convert HTML content to markdown while preserving formatting."""
    if not html_content:
        return ""
    
    # Convert <br> and <br /> to double newlines for proper markdown line breaks
    content = re.sub(r'<br\s*/?>', '\n\n', html_content)
    
    # Convert <div> tags to newlines (but not double to avoid excessive spacing)
    content = re.sub(r'</?div[^>]*>', '\n', content)
    
    # Remove all closing span tags to prevent them from showing as text (case-insensitive, optional spaces/attributes)
    content = re.sub(r'</\s*span[^>]*>', '', content, flags=re.IGNORECASE)
    
    # Remove all other HTML tags except <span> and <p>
    content = re.sub(r'<(?!span|p|/span|/p)[^>]+>', '', content)
    
    # Clean up excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Ensure proper tag closing (only for p tags now)
    content = close_tags_properly(content)
    
    # Final cleanup
    content = final_cleanup(content)
    
    return content.strip()


def final_cleanup(content):
    """Remove all literal and HTML-escaped </span> tags, case-insensitive, with optional whitespace/newlines."""
    # Remove literal </span> tags (case-insensitive, optional whitespace/newlines/attributes)
    content = re.sub(r'<\s*/\s*span[^>]*>', '', content, flags=re.IGNORECASE)
    # Remove HTML-escaped &lt;/span&gt; tags (case-insensitive, optional whitespace/newlines/attributes)
    content = re.sub(r'&lt;\s*/\s*span[^&]*&gt;', '', content, flags=re.IGNORECASE)
    return content


def clean_html_tags(content):
    """Remove unwanted HTML tags while preserving span and p tags."""
    # Remove other HTML tags but preserve span and p tags for colors and structure
    content = re.sub(r'<(?!span\b|p\b)[^>]*>', '', content)
    content = re.sub(r'</(?!span\b|p\b)>', '', content)
    
    return content


def ensure_proper_tag_closing(content):
    """Ensure all <p> tags are properly closed before the next one opens."""
    # Find all opening and closing p tags
    tag_pattern = r'<(/?)(p)([^>]*)>'
    matches = list(re.finditer(tag_pattern, content, re.IGNORECASE))
    
    # Process content character by character, tracking open p tags
    result = ""
    open_ps = []
    i = 0
    
    while i < len(content):
        # Check if we're at a tag position
        tag_found = False
        for match in matches:
            if match.start() == i:
                is_closing = bool(match.group(1))
                tag_name = match.group(2).lower()
                
                if is_closing:
                    # Closing tag - find and remove matching opening tag from stack
                    for j in range(len(open_ps) - 1, -1, -1):
                        if open_ps[j] == tag_name:
                            open_ps.pop(j)
                            break
                else:
                    # Opening tag - close any conflicting p tags first
                    if tag_name == 'p':
                        for j in range(len(open_ps) - 1, -1, -1):
                            if open_ps[j] == 'p':
                                result += '</p>'
                                open_ps.pop(j)
                    
                    # Add the new opening tag
                    open_ps.append(tag_name)
                
                # Add the tag to result
                result += match.group(0)
                i = match.end()
                tag_found = True
                break
        
        if not tag_found:
            result += content[i]
            i += 1
    
    # Close any remaining open p tags at the end
    for tag in reversed(open_ps):
        if tag == 'p':
            result += '</p>'
    
    return result


def clean_html_content(content):
    """Main function to clean and convert HTML content to clean markdown."""
    # First, unescape HTML entities
    content = html.unescape(content)
    
    # Remove Microsoft Word CSS styling
    content = remove_microsoft_word_css(content)
    
    # Handle images and links
    content, image_links = handle_images_and_links(content)
    
    # Convert HTML to markdown
    content = convert_html_to_markdown(content)
    
    # Clean unwanted HTML tags
    content = clean_html_tags(content)
    
    # Ensure proper p tag closing (but not span tags)
    content = ensure_proper_tag_closing(content)
    
    # Clean up whitespace and normalize line breaks
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = content.strip()
    
    return content, image_links


def sanitize_filename(title, date, used_filenames, author):
    """Sanitize the title to create a valid Jekyll filename."""
    # Create a slug: lowercase, replace spaces with hyphens, remove invalid chars
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)  # keep only a-z, 0-9, space, hyphen
    slug = re.sub(r'\s+', '-', slug)          # replace spaces with hyphens
    slug = re.sub(r'-+', '-', slug)            # collapse multiple hyphens
    slug = slug.strip('-')
    # Fallback if slug is empty
    if not slug:
        slug = f'{author.lower().replace(" ", "-")}-post'
    # Ensure filename starts with date
    date_prefix = date[:10]  # YYYY-MM-DD
    base_filename = f'{date_prefix}-{slug}.md'
    # Ensure uniqueness
    filename = base_filename
    counter = 1
    while filename in used_filenames:
        filename = f'{date_prefix}-{slug}-{counter}.md'
        counter += 1
    used_filenames[filename] = True
    return filename


def yaml_quote(value):
    """Quote and escape a value for YAML front matter."""
    if value is None:
        return '""'
    value = str(value)
    value = value.replace('"', '\"')
    return f'"{value}"'


def parse_xml_and_convert():
    """Parse the XML file and convert all posts."""
    # Parse the XML file
    tree = ET.parse(INPUT_XML)
    root = tree.getroot()
    
    # Define namespaces
    namespaces = {
        'atom': 'http://www.w3.org/2005/Atom',
        'gd': 'http://schemas.google.com/g/2005',
        'thr': 'http://purl.org/syndication/thread/1.0'
    }
    
    # Find all entries first
    all_entries = root.findall('.//atom:entry', namespaces)
    print(f"Found {len(all_entries)} total entries")
    
    # Find all blog posts (entries with post kind)
    posts = []
    for entry in all_entries:
        # Check if this is a blog post (not a template or other entry type)
        category_elem = entry.find('atom:category[@term="http://schemas.google.com/blogger/2008/kind#post"]', namespaces)
        if category_elem is not None:
            posts.append(entry)
    
    print(f"Found {len(posts)} blog posts")
    
    converted_count = 0
    used_filenames = {}  # Track used filenames to avoid duplicates
    
    for post in posts:
        # Extract post metadata
        title_elem = post.find('atom:title', namespaces)
        if title_elem is None or title_elem.text is None:
            title = "Untitled"
        else:
            title = title_elem.text.strip()
            if not title:
                title = "Untitled"
        
        # Extract publication date
        published_elem = post.find('atom:published', namespaces)
        if published_elem is None:
            continue
            
        published_date = published_elem.text[:10]  # YYYY-MM-DD
        
        # Extract author
        author_elem = post.find('.//atom:author/atom:name', namespaces)
        author = author_elem.text if author_elem is not None else "Unknown"
        
        # Skip Thomas Domingues' and Unknown authors posts
        if author == "Thomas Domingues" or author == "Unknown":
          continue
        
        # Extract last modified date
        updated_elem = post.find('atom:updated', namespaces)
        last_modified = updated_elem.text if updated_elem is not None else published_elem.text
        
        # Extract content
        content_elem = post.find('atom:content', namespaces)
        if content_elem is None:
            continue
            
        content = content_elem.text
        
        # Clean and convert content
        cleaned_content, image_links = clean_html_content(content)
        
        # Create filename with better handling of problematic titles
        filename = sanitize_filename(title, published_date, used_filenames, author)
        
        # Prepare front matter as a dict
        front_matter = {
            'layout': 'poem',
            'title': title,
            'date': published_elem.text,
            'author': author,
            'last_modified_at': last_modified,
            'categories': ['imported', 'blogspot'],
            'tags': ['blogspot', author]
        }
        if image_links:
            front_matter['images'] = image_links
        
        # Write to file with manual YAML front matter
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('---\n')
            for key, value in front_matter.items():
                if isinstance(value, list):
                    f.write(f'{key}:\n')
                    for item in value:
                        f.write(f'  - {yaml_quote(item)}\n')
                else:
                    f.write(f'{key}: {yaml_quote(value)}\n')
            f.write('---\n\n')
            f.write(cleaned_content)
        
        print(f"Converted '{title}' and saved to {filename}")
        converted_count += 1
    
    print(f"\nProcessing complete! Converted {converted_count} posts.")


if __name__ == "__main__":
    parse_xml_and_convert()
    print("Processing complete!")
