import re

with open('anka_full_original.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<section class="page-section[^"]*" data-page="tab-6">(.*?)</section>'
match = re.search(pattern, content, re.DOTALL)
if match:
    s6 = match.group(1)
    inputs = re.findall(r'<input\b([^>]*)>', s6)
    print(f"Tab 6 has {len(inputs)} inputs:")
    for i, inp in enumerate(inputs, 1):
        id_m = re.search(r'id="([^"]*)"', inp)
        ans_m = re.search(r'data-answer="([^"]*)"', inp)
        print(f"  {i}: id={id_m.group(1) if id_m else 'NONE'}, answer={ans_m.group(1) if ans_m else 'NONE'}")
