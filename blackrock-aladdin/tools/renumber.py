import sys, re
from html.parser import HTMLParser
F = sys.argv[1]
html = open(F, encoding="utf-8").read()
head, body = html.split('</head>', 1)
reg_start = body.index('<div class="register">')
reg_end = body.index('</div>\n</section>', reg_start)
pre, register, post = body[:reg_start], body[reg_start:reg_end], body[reg_end:]

# --- parse body citations with html.parser (order of appearance) ---
class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.in_sup = False; self.refs = []; self.ids = []; self.cur = None; self.text = ''
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'sup' and a.get('class') == 'fnref': self.in_sup = True
        if tag == 'a' and self.in_sup: self.cur = a.get('href'); self.text = ''
        if tag == 'p' and a.get('id', '').startswith('s'): self.ids.append(a['id'])
    def handle_data(self, d):
        if self.cur: self.text += d
    def handle_endtag(self, tag):
        if tag == 'a' and self.cur:
            self.refs.append((self.cur, self.text.strip())); self.cur = None
        if tag == 'sup': self.in_sup = False
p = P(); p.feed(pre + post)  # citations outside the register
q = P(); q.feed(register)
ids = set(q.ids)
assert not p.ids
bad = [(h, t) for h, t in p.refs if h != '#s' + t or h[1:] not in ids]
assert not bad, bad
cited = []
for h, t in p.refs:
    if h[1:] not in cited: cited.append(h[1:])
orphans = sorted(ids - set(cited), key=lambda s: int(s[1:]))
print('cited', len(cited), 'register', len(ids), 'orphans', orphans)
assert not orphans
mapping = {old: f's{i+1}' for i, old in enumerate(cited)}
changed = {o: n for o, n in mapping.items() if o != n}
print('entries renumbered:', len(changed))

# --- rewrite refs and ids with a single regex pass (token-safe) ---
def rw_refs(s):
    return re.sub(r'<a href="#(s\d+)">(\d+)</a>', lambda m: f'<a href="#{mapping[m.group(1)]}">{mapping[m.group(1)][1:]}</a>', s)
pre2, post2 = rw_refs(pre), rw_refs(post)
assert pre2.count('<a href="#s') == pre.count('<a href="#s')

# register: rewrite ids/numbers, then re-sort entries within each grade group
def rw_entry(m):
    old = m.group(1); new = mapping[old]
    return m.group(0).replace(f'<p id="{old}"><b class="n">{old[1:]}</b>', f'<p id="{new}"><b class="n">{new[1:]}</b>', 1)
register2 = re.sub(r'<p id="(s\d+)"><b class="n">\d+</b>.*?</p>', rw_entry, register, flags=re.S)
parts = re.split(r'(<h3>.*?</h3>\n)', register2)
out = [parts[0]]
for i in range(1, len(parts), 2):
    h3, block = parts[i], parts[i+1]
    entries = re.findall(r'<p id="s\d+">.*?</p>\n', block, flags=re.S)
    assert ''.join(entries) == block, (h3, len(entries), len(block), len(''.join(entries)))
    entries.sort(key=lambda e: int(re.match(r'<p id="s(\d+)"', e).group(1)))
    out.append(h3 + ''.join(entries))
register3 = ''.join(out)
new_html = head + '</head>' + pre2 + register3 + post2
# final verification
r = P(); r.feed(new_html.split('</head>')[1])
ids2 = set(r.ids); refs2 = [(h, t) for h, t in r.refs]
assert all(h == '#s' + t and h[1:] in ids2 for h, t in refs2), 'dangling after renumber'
order = []
for h, t in refs2:
    if h[1:] not in order: order.append(h[1:])
assert order == [f's{i+1}' for i in range(len(order))], order[:10]
assert ids2 == set(order)
assert len(re.findall(r'<p id="s', new_html)) == len(ids)
open(F, 'w', encoding='utf-8').write(new_html)
print('first-citation order verified; wrote', F)
