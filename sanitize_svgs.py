import os
import re
import glob

# Directory containing the SVGs
svg_dir = 'assets/media/icons/custom/'

# Regex to find id="xxx" and url(#xxx)
id_pattern = re.compile(r'id="([^"]+)"')
url_pattern = re.compile(r'url\(#([^)]+)\)')
href_pattern = re.compile(r'xlink:href="#([^"]+)"')

for filepath in glob.glob(os.path.join(svg_dir, '*.svg')):
    filename = os.path.basename(filepath)
    name, ext = os.path.splitext(filename)
    
    # Read SVG
    with open(filepath, 'r') as f:
        content = f.read()

    # Find all IDs defined in this file
    ids = id_pattern.findall(content)
    
    # We will prefix them with the filename (e.g. bash_clip1)
    # But only if it hasn't been prefixed yet
    for original_id in set(ids):
        # We don't want to prefix if it's already prefixed
        if not original_id.startswith(name + '_'):
            new_id = f"{name}_{original_id}"
            # Replace id="id"
            content = content.replace(f'id="{original_id}"', f'id="{new_id}"')
            # Replace url(#id)
            content = content.replace(f'url(#{original_id})', f'url(#{new_id})')
            # Replace xlink:href="#id"
            content = content.replace(f'xlink:href="#{original_id}"', f'xlink:href="#{new_id}"')

    # Save SVG
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Sanitized {filename}")
