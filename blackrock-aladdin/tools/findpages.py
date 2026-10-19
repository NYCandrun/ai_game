#!/usr/bin/env python3
"""Find the PDF page of each part divider and chapter heading; write pages.json."""
import sys, re, json, subprocess
pdf, md, out = sys.argv[1:4]
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
pages = []
for i in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout
    pages.append(re.sub(r'\s+', ' ', t.replace('’', "'")).strip())
# headings from the markdown
entries = []
part = 0
for l in open(md, encoding='utf-8'):
    if l.startswith('# '):
        part += 1; entries.append(('part-%d' % part, 'Part %d %s' % (part, l[2:].strip()), 'part'))
    elif l.startswith('## ') and l[3:].strip() != 'Contents':
        h = l[3:].strip(); m = re.match(r'(\d+)\. (.*)', h)
        entries.append(('c%s' % m.group(1) if m else re.sub(r'[^a-z0-9]+', '-', h.lower()).strip('-'), h, 'chapter'))
entries = [('executive-summary' if e[0] == 'summary' else e[0], e[1], e[2]) for e in entries]
res = {}
start = 3  # skip cover and contents
last_part_page = 0
for cid, text, kind in entries:
    text = text.replace('’', "'")
    found = None
    for i in range(start - 1, n):
        if kind == 'chapter' and i + 1 <= last_part_page:
            continue
        if pages[i].startswith(text):
            found = i + 1; break
    if found is None:
        for i in range(start - 1, n):
            if kind == 'chapter' and i + 1 <= last_part_page:
                continue
            if text in pages[i]:
                found = i + 1; break
    if found is None:
        print('NOT FOUND', cid, text); continue
    res[cid] = found
    if kind == 'part': last_part_page = found
    start = found
json.dump(res, open(out, 'w'), indent=1)
print(res)
