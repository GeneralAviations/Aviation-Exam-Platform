import re
import json

with open('anka_full_original.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to capture each section
pattern = r'(<section class="page-section[^"]*" data-page="([^"]+)">.*?</section>)'
matches = re.findall(pattern, content, re.DOTALL)
print(f"Extracted {len(matches)} sections:")
for full_html, page in matches:
    print(f"  {page}: {len(full_html)} bytes")
