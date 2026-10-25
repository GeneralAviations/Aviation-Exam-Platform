import re
import json

with open('anka_full_original.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section class="page-section[^"]*" data-page="([^"]+)">(.*?)</section>', html, re.DOTALL)
print(f"Found {len(sections)} sections in anka_full_original.html:")
for spage, scontent in sections:
    inputs = re.findall(r'<input\b[^>]*>', scontent)
    print(f"  {spage}: {len(inputs)} inputs")

with open('data/anka-male-uav.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

sec_map = {
    'tab-1': 'BOLD FACE LIMITATIONS',
    'tab-2': 'EMER - ACT POSITION FAIL',
    'tab-3': 'EMER - ENG RPM HIGH',
    'tab-4': 'EMER - ENG RPM LOW',
    'tab-5': 'EMER - LDG GR EXTENTION FAIL',
    'tab-6': 'EMER - ENG STOPPED'
}

for tab, sname in sec_map.items():
    qs = [q for q in d['questions'] if q['section'] == sname]
    print(f"JSON {sname} ({tab}): {len(qs)} questions")
