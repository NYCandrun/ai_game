import re, sys, subprocess
H, P = sys.argv[1], sys.argv[2]
html = open(H, encoding='utf-8').read()
npages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', P], capture_output=True, text=True).stdout).group(1))
pages = [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), P, '-'], capture_output=True, text=True).stdout for i in range(1, npages+1)]
def find(text, start=1):
    t = re.sub(r'\s+', ' ', text).strip()
    for i in range(start-1, npages):
        if t in re.sub(r'\s+', ' ', pages[i]):
            return i+1
    return None
# chapter headings (h2) in order
h2s = re.findall(r'<h2 id="([^"]*)">([^<]*)</h2>', html)
chap = {}
last = 3
for hid, txt in h2s:
    pg = find(txt, last)
    chap[hid] = pg
    if pg: last = pg
# part dividers: pages whose first non-empty line is "Part N" / "Appendices"
parts = {}
for i, t in enumerate(pages):
    lines = [l for l in t.splitlines() if l.strip()]
    if lines and re.match(r'^(Part \d|Appendices)$', lines[0].strip()):
        parts[lines[0].strip()] = i+1
print("chapters:", chap); print("parts:", parts)
# map anchors -> pages
anchor_page = {}
for hid, txt in h2s:
    anchor_page[hid] = chap[hid]
# also allow links by slug ids: find <section ... id="slug"> containing h2 id
secs = [(m.start(), m.group(1)) for m in re.finditer(r'<section[^>]*id="([^"]*)"', html)]
for i, (pos, sid) in enumerate(secs):
    end = secs[i+1][0] if i+1 < len(secs) else len(html)
    m = re.search(r'<h2 id="([^"]*)"', html[pos:end])
    if m and m.group(1) in chap: anchor_page[sid] = chap[m.group(1)]
def pgfor(href):
    a = href.lstrip('#')
    if a in anchor_page and anchor_page[a]: return anchor_page[a]
    if a.startswith('part-'):
        n = re.match(r'part-(\d)', a)
        return parts.get('Part '+n.group(1)) if n else None
    if a == 'appendices': return parts.get('Appendices')
    return None
# rewrite every pg span (broken or not) in toc and chapters lists
cnt = 0; miss = []
def rep(m):
    global cnt
    href = m.group(2); pg = pgfor(href)
    if pg is None:
        miss.append(href); return m.group(0)
    cnt += 1
    return f'{m.group(1)}<span class="pg">{pg}</span></li>'
html2 = re.sub(r'(<a href="(#[^"]*)">[^<]*</a></span>)<span class="pg">[^<]*(?:</span>)?</li>', rep, html)
print("rewrote", cnt, "missing", miss)
open(H, 'w', encoding='utf-8').write(html2)
