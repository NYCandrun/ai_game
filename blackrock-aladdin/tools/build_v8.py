#!/usr/bin/env python3
"""Build the BlackRock-styled HTML edition of the V8 Markdown.

Usage: build_v8.py <md> <head_src.html> <out.html> [pages.json]
The head (lines 1-468 of key_findings_original.html) is copied verbatim.
"""
import sys, re, json, html

MD, HEAD_SRC, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
PAGES = {}
RUNON = set()
if len(sys.argv) > 5:
    RUNON = set(json.load(open(sys.argv[5])))
if len(sys.argv) > 4:
    try:
        PAGES = json.load(open(sys.argv[4]))
    except Exception:
        PAGES = {}

def pg(key):
    return str(PAGES.get(key, "0"))

# ------------------------------------------------------------------ inline
LINK_DOMAINS = r'(?:github\.com|youtube\.com|blackrock\.com|careers\.blackrock\.com|engineering\.blackrock\.com|press\.aboutamazon\.com|learn\.microsoft\.com|pandas\.pydata\.org|snowflake\.com|fivetran\.com|microsoft\.com|zenml\.io|linter\.aip\.dev|google\.aip\.dev|pypi\.org|inspector\.pypi\.io|aip\.dev)'

def esc(s):
    return html.escape(s, quote=False)

def stag_sub(m):
    run = m.group(1)
    # split into individual tags / ranges
    parts = re.findall(r'S\d{1,3}(?:\s[–-]\s?S\d{1,3})?', run)
    out = []
    for p in parts:
        first = re.match(r'S\d{1,3}', p).group(0)
        out.append('<a class="stag" href="#%s">%s</a>' % (first, p.replace(' ', '&#8201;')))
    return ' '.join(out)

STAG_RE = re.compile(r'(?<![A-Za-z0-9#/_-])((?:S\d{1,3}(?:\s[–-]\s?S\d{1,3})?)(?:\sS\d{1,3}(?:\s[–-]\s?S\d{1,3})?)*)(?![A-Za-z0-9_-])(?!\s(?:Storage|is a widely))')

def inl(s, tags=True):
    s = esc(s)
    # apostrophes between letters
    s = re.sub(r"(?<=\w)'(?=\w)", "’", s)
    # bold / italic
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    # explicit domain/path strings become links
    s = re.sub(r'(?<![\w/])(' + LINK_DOMAINS + r'/[^\s;,)<]+?)(?=[.,;)]?(?:\s|$|<))',
               lambda m: '<a href="https://%s">%s</a>' % (m.group(1), m.group(1)), s)
    if tags:
        s = STAG_RE.sub(stag_sub, s)
    return s

# ------------------------------------------------------------------ parse
lines = open(MD, encoding='utf-8').read().split('\n')
# front matter
assert lines[0] == '---'
fm_end = lines.index('---', 1)
fm = {}
for l in lines[1:fm_end]:
    k, v = l.split(':', 1)
    fm[k.strip()] = v.strip().strip('"')
body_lines = lines[fm_end + 1:]

blocks = []  # (type, payload)
i = 0
while i < len(body_lines):
    l = body_lines[i]
    if not l.strip():
        i += 1; continue
    if l.startswith('#'):
        m = re.match(r'(#+)\s+(.*)', l)
        blocks.append(('h%d' % len(m.group(1)), m.group(2).strip()))
        i += 1; continue
    if l.startswith('|'):
        rows = []
        while i < len(body_lines) and body_lines[i].startswith('|'):
            rows.append(body_lines[i]); i += 1
        cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
        header = cells[0]; data = [r for r in cells[2:]]
        blocks.append(('table', (header, data)))
        continue
    if re.match(r'^- ', l):
        items = []
        while i < len(body_lines) and re.match(r'^- ', body_lines[i]):
            items.append(body_lines[i][2:].strip()); i += 1
        blocks.append(('ul', items)); continue
    if re.match(r'^\d+\. ', l):
        items = []
        while i < len(body_lines) and re.match(r'^\d+\. ', body_lines[i]):
            items.append(re.sub(r'^\d+\. ', '', body_lines[i]).strip()); i += 1
        blocks.append(('ol', items)); continue
    para = []
    while i < len(body_lines) and body_lines[i].strip() and not body_lines[i].startswith(('#', '|', '- ')) and not re.match(r'^\d+\. ', body_lines[i]):
        para.append(body_lines[i].strip()); i += 1
    blocks.append(('p', ' '.join(para)))

# ------------------------------------------------------------------ helpers
def slug(s):
    s = re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
    return s

NUM_RE = re.compile(r'^[\d.,%–-]+$')

def is_num_col(data, ci):
    vals = [r[ci] for r in data if ci < len(r)]
    return all(NUM_RE.match(v) or v == '' for v in vals) and any(NUM_RE.match(v) for v in vals)

def render_table(header, data, first_bold=True, cls='', widths=None, hl_rows=(), cell_hook=None, no_thead=False, tags=True):
    ncol = len(header)
    numcols = [ci for ci in range(ncol) if is_num_col(data, ci)]
    out = ['<table%s>' % (' class="%s"' % cls if cls else '')]
    if widths:
        out.append('<colgroup>' + ''.join('<col%s>' % (' style="width:%s"' % w if w else '') for w in widths) + '</colgroup>')
    if not no_thead and any(h for h in header):
        out.append('<thead><tr>' + ''.join('<th%s>%s</th>' % (' class="num"' if ci in numcols else '', inl(h, tags)) for ci, h in enumerate(header)) + '</tr></thead>')
    out.append('<tbody>')
    for ri, r in enumerate(data):
        trcls = ' class="hl"' if ri in hl_rows else ''
        tds = []
        for ci in range(ncol):
            v = r[ci] if ci < len(r) else ''
            classes = []
            if ci == 0 and first_bold: classes.append('first')
            if ci in numcols: classes.append('num')
            content = inl(v, tags)
            if cell_hook:
                content, classes = cell_hook(ri, ci, v, content, classes)
            tds.append('<td%s>%s</td>' % (' class="%s"' % ' '.join(classes) if classes else '', content))
        out.append('<tr%s>%s</tr>' % (trcls, ''.join(tds)))
    out.append('</tbody></table>')
    return '\n'.join(out)

def lbl_text(s):
    """Turn a leading **STATED** / **INFERENCE · X** into a label marker."""
    m = re.match(r'\*\*(STATED|INFERENCE · [A-Z]+)\*\*\s*(.*)', s)
    if not m:
        return None
    lab, rest = m.group(1), m.group(2)
    cls = 'lbl' if lab == 'STATED' else 'lbl e'
    return '<span class="%s"><strong>%s</strong></span> %s' % (cls, esc(lab), inl(rest))

def hbar_chart(rows, label_w=150, width=504, row_h=22, bar_h=16, legend=None, scale_max=None, aria='', val_w=70):
    """rows: list of dicts {label, total, part (or None), text, cls} ; part drawn yellow, remainder gray.
    cls 'hl' -> whole bar yellow; 'core' -> dashed outline."""
    top = 20 if legend else 4
    h = top + row_h * len(rows) + 4
    mx = scale_max or max(r['total'] for r in rows)
    bar_w = width - label_w - val_w
    o = ['<svg class="chart" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg" width="%dpt" height="%.1fpt" viewBox="0 0 %d %.1f">' % (esc(aria), width, h, width, h)]
    if legend:
        x = label_w
        for col, txt in legend:
            o.append('<rect x="%.1f" y="4" width="8.5" height="8.5" fill="%s"/>' % (x, col))
            o.append('<text x="%.1f" y="11.7" font-size="9">%s</text>' % (x + 12, esc(txt)))
            x += 12 + 4.4 * len(txt) + 14
    for i, r in enumerate(rows):
        y = top + i * row_h
        by = y + (row_h - bar_h) / 2
        tot_w = bar_w * r['total'] / mx
        if r.get('cls') == 'core':
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="#F2F2F2" stroke="#000" stroke-width="0.75" stroke-dasharray="2 2"/>' % (label_w, by, tot_w, bar_h))
        elif r.get('part') is not None:
            pw = bar_w * r['part'] / mx
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="#FFCE00"/>' % (label_w, by, pw, bar_h))
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="#D6D5DD"/>' % (label_w + pw, by, tot_w - pw, bar_h))
        else:
            fill = '#FFCE00' if r.get('cls') == 'hl' else '#D6D5DD'
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" fill="%s"/>' % (label_w, by, tot_w, bar_h, fill))
        o.append('<text x="%.1f" y="%.1f" font-size="9" text-anchor="end"%s>%s</text>' % (label_w - 8, by + bar_h - 4.5, ' font-weight="700"' if r.get('cls') == 'hl' else '', esc(r['label'])))
        o.append('<text x="%.1f" y="%.1f" font-size="9" font-weight="700">%s</text>' % (label_w + tot_w + 4, by + bar_h - 4.5, esc(r['text'])))
    o.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#000" stroke-width="0.75"/>' % (label_w, label_w, top - 2, h - 2))
    o.append('</svg>')
    return '\n'.join(o)

def timeline_svg():
    # months from Jan 2024 (0) to Dec 2026 (35)
    import datetime as dt
    x0, x1, width = 140, 496, 504
    d0, d1 = dt.date(2024, 1, 1), dt.date(2027, 1, 1)
    def X(d):
        return x0 + (x1 - x0) * (d - d0).days / (d1 - d0).days
    o = ['<svg class="chart" role="img" aria-label="Timeline of PyPI releases: the core package from May 2024 to July 27, 2026 (14 releases); the 11 API add-ons on July 17, 2024 and January 22, 2026; report date October 18, 2026." xmlns="http://www.w3.org/2000/svg" width="504pt" height="118pt" viewBox="0 0 504 118">']
    # year axis
    ay = 100
    o.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#000" stroke-width="0.75"/>' % (x0, x1, ay, ay))
    for yr in (2024, 2025, 2026):
        xa, xb = X(dt.date(yr, 1, 1)), X(dt.date(yr + 1, 1, 1))
        o.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#000" stroke-width="0.75"/>' % (xa, xa, ay, ay + 4))
        o.append('<text x="%.1f" y="%d" font-size="9" text-anchor="middle">%d</text>' % ((xa + xb) / 2, ay + 14, yr))
        for q in (4, 7, 10):
            xq = X(dt.date(yr, q, 1))
            o.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#000" stroke-width="0.5"/>' % (xq, xq, ay, ay + 2))
    o.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#000" stroke-width="0.75"/>' % (x1, x1, ay, ay + 4))
    # lanes
    lanes = [('Core package, aladdinsdk', 30), ('11 API add-ons', 70)]
    for lab, y in lanes:
        o.append('<text x="%d" y="%.1f" font-size="9" font-weight="700" text-anchor="end">%s</text>' % (x0 - 10, y + 3.5, lab))
        o.append('<line x1="%.1f" x2="%.1f" y1="%d" y2="%d" stroke="#D6D5DD" stroke-width="0.75"/>' % (x0, x1, y, y))
    # core: band May 2024 -> Jul 27 2026
    ca, cb = X(dt.date(2024, 5, 1)), X(dt.date(2026, 7, 27))
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="10" fill="#FFCE00"/>' % (ca, 25, cb - ca))
    o.append('<text x="%.1f" y="%d" font-size="8" font-family="Barlow Condensed" text-anchor="middle">14 releases, beta and alpha</text>' % ((ca + cb) / 2, 19))
    o.append('<text x="%.1f" y="%d" font-size="8" font-family="Barlow Condensed" text-anchor="start">May 2024</text>' % (ca, 46))
    o.append('<text x="%.1f" y="%d" font-size="8" font-family="Barlow Condensed" text-anchor="end">2.0.0b10, Jul 27, 2026</text>' % (cb, 46))
    # add-ons: two dots, dashed gap
    aa, ab = X(dt.date(2024, 7, 17)), X(dt.date(2026, 1, 22))
    o.append('<line x1="%.1f" x2="%.1f" y1="70" y2="70" stroke="#7F7F7F" stroke-width="0.75" stroke-dasharray="2 2"/>' % (aa, ab))
    for xx in (aa, ab):
        o.append('<circle cx="%.1f" cy="70" r="4.5" fill="#FFCE00" stroke="#000" stroke-width="0.75"/>' % xx)
    o.append('<text x="%.1f" y="59" font-size="8" font-family="Barlow Condensed" text-anchor="middle">18 months with no add-on release</text>' % ((aa + ab) / 2))
    o.append('<text x="%.1f" y="86" font-size="8" font-family="Barlow Condensed" text-anchor="middle">Jul 17, 2024</text>' % aa)
    o.append('<text x="%.1f" y="86" font-size="8" font-family="Barlow Condensed" text-anchor="middle">Jan 22, 2026</text>' % ab)
    # report date
    rd = X(dt.date(2026, 10, 18))
    o.append('<line x1="%.1f" x2="%.1f" y1="12" y2="%d" stroke="#FF4713" stroke-width="0.75" stroke-dasharray="3 2"/>' % (rd, rd, ay))
    o.append('<text x="%.1f" y="9" font-size="8" font-family="Barlow Condensed" text-anchor="end" fill="#FF4713">Report date, Oct 18, 2026</text>' % (rd + 2))
    o.append('</svg>')
    return '\n'.join(o)

# ------------------------------------------------------------------ structure
TOC = []  # entries: dict(kind='part'|'chapter', id, n, title, desc)
out = []
W = out.append

def chapter_id(title):
    m = re.match(r'(\d+)\. (.*)', title)
    if m:
        return 'c%s' % m.group(1)
    if title == 'Summary':
        return 'executive-summary'
    return slug(title)

# Pre-scan headings for the contents and cover
parts_desc = {}
for bi, (t, p) in enumerate(blocks):
    if t == 'table' and p[0] == ['Part', 'What it holds']:
        for r in p[1]:
            parts_desc[r[0].strip('*')] = r[1]
part_n = 0
for t, p in blocks:
    if t == 'h1':
        part_n += 1
        TOC.append(dict(kind='part', id='part-%d' % part_n, n=part_n, title=p, desc=parts_desc.get(p, '')))
    elif t == 'h2' and p != 'Contents':
        m = re.match(r'(\d+)\. (.*)', p)
        TOC.append(dict(kind='chapter', id=chapter_id(p), n=m.group(1) if m else '', title=m.group(2) if m else p))

# ------------------------------------------------------------------ cover
intro_para = blocks[0][1]
indep_line = blocks[1][1].strip('*')
W('</head>')
W('<body>')
W('<section class="fullpage cover">')
W('  <p class="prepared-for">Prepared for BlackRock</p>')
W('  <div class="inner">')
W('    <span class="accent-bar"></span>')
W('    <h1>%s</h1>' % esc(fm['title']))
W('    <p class="subtitle">%s</p>' % esc(fm['subtitle']))
W('    <p class="meta">Prepared by <strong>Jacob Nikolau</strong>&emsp;|&emsp;As of October 18, 2026 · V8 revision October 19, 2026</p>')
W('  </div>')
W('  <div class="parts">')
for e in [e for e in TOC if e['kind'] == 'part']:
    W('<div><span class="accent-bar"></span><p class="pn">Part %d</p><p class="pt"><a href="#%s">%s</a></p><p class="pc">%s</p><p class="pc">Page %s</p></div>' % (e['n'], e['id'], esc(e['title']), inl(e['desc']), pg(e['id'])))
W('  </div>')
W('  <p class="indep">%s</p>' % esc(indep_line))
W('</section>')

# ------------------------------------------------------------------ contents
W('<section class="contents" id="contents">')
W('  <h2>Contents</h2>')
W('  <p class="front-note">%s</p>' % inl(intro_para))
W('  <ul class="toc">')
for e in TOC:
    if e['kind'] == 'part':
        W('<li class="part"><span class="n"></span><span><a href="#%s">Part %d. %s</a> <span class="part-desc">%s</span></span><span class="pg">%s</span></li>' % (e['id'], e['n'], esc(e['title']), inl(e['desc']), pg(e['id'])))
    else:
        W('<li class=""><span class="n">%s</span><span><a href="#%s">%s</a></span><span class="pg">%s</span></li>' % (e['n'], e['id'], esc(e['title']), pg(e['id'])))
W('  </ul>')
W('''  <div class="label-key">
    <h3>How to read the labels</h3>
    <p>Each conclusion separates what the files state from what is inferred. A black square marks a <strong>Stated</strong> claim: the package files, or PyPI’s public records about them, say this directly. An orange square marks an <strong>Inference</strong>, rated Strong, Moderate or Tentative by how firmly the evidence supports it. Small S tags, such as <a class="stag" href="#S1">S1</a>, point to the sources sheet in the Reference part.</p>
    <div class="key-grid"><div><span class="key-ex"><span class="lbl">Stated</span></span><span>The package files, or PyPI’s public records about them, say this directly.</span></div><div><span class="key-ex"><span class="lbl e">Inference · Strong</span></span><span>Several separate clues point the same way, and nothing in the files points the other way.</span></div><div><span class="key-ex"><span class="lbl e">Inference · Moderate</span></span><span>The clues fit, but another explanation is still possible.</span></div><div><span class="key-ex"><span class="lbl e">Inference · Tentative</span></span><span>The conclusion rests on one clue, or on something the files leave out.</span></div></div>
  </div>''')
W('</section>')

# ------------------------------------------------------------------ body walk
state = dict(in_chapter=False, in_figure=False, fig_no=None, chapter=None, in_sources=False, part=0, kh=0)
bi = 0
# skip intro, indep line, '## Contents', contents table
while bi < len(blocks) and not (blocks[bi][0] == 'h1'):
    bi += 1

def close_figure():
    if state['in_figure']:
        W('</figure>')
        state['in_figure'] = False
        state['fig_no'] = None

def close_kh():
    if state['kh'] > 0:
        W('</div>')
        state['kh'] = 0

def close_chapter():
    close_figure()
    close_kh()
    if state['in_chapter']:
        W('</section>')
        state['in_chapter'] = False

def stats_row(header, data, src=None):
    o = ['<div class="stats">']
    for n, cap in zip(header, data[0]):
        o.append('<div><span class="accent-bar"></span><p class="num">%s</p><p class="cap">%s</p></div>' % (esc(n), inl(cap)))
    o.append('</div>')
    return '\n'.join(o)

def exhibit_open(no, title, cls=''):
    state['in_figure'] = True
    state['fig_no'] = no
    W('<figure class="exhibit%s" id="exhibit-%d">' % ((' ' + cls) if cls else '', no))
    W('<p class="ex-title"><span class="ex-num">Exhibit %d.</span> %s</p>' % (no, inl(title)))

def notes(text):
    W('<div class="notes"><p>%s</p></div>' % inl(text))

# Exhibit-specific builders. Each consumes blocks from bi up to and including the Source paragraph.
def take_until_source(start):
    j = start
    seg = []
    while j < len(blocks):
        t, p = blocks[j]
        seg.append(blocks[j]); j += 1
        if t == 'p' and p.startswith('Source:'):
            break
    return seg, j

def build_ex2(seg):
    # seg: table(who/how/where), p(Add-on APIs), p(*Where the APIs reach*), table(6 areas), p(SQL...), p(*One Studio job*), table(steps), p(The files do not), p(Source)
    tb1 = seg[0][1]; addon = seg[1][1]; sub1 = seg[2][1].strip('*'); tb2 = seg[3][1]; adc = seg[4][1]; job = seg[5][1]; steps = seg[6][1]; after = seg[7][1]; src = seg[8][1]
    def hook1(ri, ci, v, content, classes):
        if ci == 0: classes = ['first']
        return content, classes
    hdr = tb1[0][:]
    hdr[2] = hdr[2].replace('(Inference)', '')
    tbl = render_table(hdr, tb1[1], widths=['44pt', None, None], cell_hook=hook1)
    tbl = tbl.replace('<th>Studio builders </th>', '<th>Studio builders <span class="lbl e">Inference</span></th>')
    tbl = tbl.replace('<strong>Aladdin Studio</strong> (Inference):', '<strong>Aladdin Studio</strong> <span class="lbl e">Inference</span>:')
    W('<div class="tbl-wrap">' + tbl + '</div>')
    W('<p class="ex-legend"><strong>%s</strong></p>' % inl(addon))
    W('<p class="ex-sub">%s</p>' % inl(sub1))
    W('<div class="tbl-wrap areas">' + render_table(tb2[0], tb2[1], first_bold=False) + '</div>')
    adc_html = inl(adc).replace('<em>Inference: programs likely pull large data sets from here.</em>', '<span class="lbl e">Inference: programs likely pull large data sets from here.</span>')
    W('<div class="band">%s</div>' % adc_html)
    W('<p class="ex-sub">%s</p>' % inl(job))
    def hook_steps(ri, ci, v, content, classes):
        if ci == 0:
            return '<span class="step">%s</span>' % esc(v), ['ctr']
        if ci == 2:
            cls = 'lbl' if v == 'Stated' else 'lbl e'
            return '<span class="%s">%s</span>' % (cls, esc(v)), []
        return content, classes
    W('<div class="tbl-wrap">' + render_table(steps[0], steps[1], first_bold=False, widths=['30pt', None, '70pt'], cell_hook=hook_steps) + '</div>')
    W('<p class="ex-legend">%s</p>' % inl(after))
    notes(src)

def build_ex3(seg):
    tb = seg[0][1]; src = seg[1][1]
    rows = []
    for r in tb[1]:
        tot = int(r[1]); share = int(r[2].rstrip('%'))
        rows.append(dict(label=r[0], total=tot, part=round(tot * share / 100), text='%d · %s' % (tot, r[2]), cls='core' if r[0] == 'Core package' else None))
    svg = hbar_chart(rows, label_w=110, width=300, legend=[('#FFCE00', 'Change'), ('#D6D5DD', 'Read or check')], aria='Horizontal bar chart of operations in each package, with the share that change something: ' + '; '.join('%s %d, %s' % (r[0], int(r[1]), r[2]) for r in tb[1]) + '.')
    W('<div class="chart-row"><div>' + svg + '</div><div class="side">')
    W(render_table(tb[0], tb[1], hl_rows=(0,)))
    W('</div></div>')
    notes(src)

def build_ex4(seg):
    head = seg[0][1]; tb = seg[1][1]; para = seg[2][1]; src = seg[3][1]
    m = re.match(r'(Aladdin Studio) \((Inference: .*)\)$', head)
    W('<div class="studio-box"><p class="studio-head"><strong>%s</strong> <span class="lbl e">%s</span></p>' % (esc(m.group(1)), esc(m.group(2))))
    W(render_table(tb[0], tb[1], widths=['120pt', None]))
    W('</div>')
    W('<p class="ex-legend">%s</p>' % inl(para))
    notes(src)

def build_ex8(seg):
    sub1 = seg[0][1]; tb1 = seg[1][1]; sub2 = seg[2][1]; tb2 = seg[3][1]; src = seg[4][1]
    rows = []
    for r in tb1[1] + tb2[1]:
        ops, apis = int(r[1]), int(r[2])
        rows.append(dict(label=r[0], total=ops, text='%d operations · %d APIs' % (ops, apis), cls='core' if r[0] == 'Core package' else ('hl' if r[0] == 'Operations' else None)))
    svg = hbar_chart(rows, label_w=120, width=504, legend=[('#FFCE00', 'Operations, the largest area'), ('#D6D5DD', 'Other areas'), ('#F2F2F2', 'Core package')], val_w=118, aria='Horizontal bar chart of operations by area: ' + '; '.join('%s %s operations, %s APIs' % (r[0], r[1], r[2]) for r in tb1[1] + tb2[1]) + '.')
    W(svg)
    W('<p class="ex-sub">%s</p>' % inl(sub1))
    W('<div class="tbl-wrap">' + render_table(tb1[0], tb1[1], widths=['74pt', '46pt', '30pt', None, '110pt'], hl_rows=(4,)) + '</div>')
    W('<p class="ex-sub">%s</p>' % inl(sub2))
    W('<div class="tbl-wrap">' + render_table(tb2[0], tb2[1], widths=['74pt', '46pt', '30pt', None, '110pt']) + '</div>')
    notes(src)

def build_ex9(seg):
    tb = seg[0][1]; para = seg[1][1]; src = seg[2][1]
    W(stats_row(tb[0], tb[1]))
    W('<p class="ex-legend">%s</p>' % inl(para))
    notes(src)

def build_ex12(seg):
    tb = seg[0][1]; rd = seg[1][1]; src = seg[2][1]
    W(timeline_svg())
    W('<div class="tbl-wrap">' + render_table(tb[0], tb[1], widths=['150pt', '110pt', None]) + '</div>')
    W('<p class="ex-legend">%s</p>' % inl(rd))
    notes(src)

GENERIC_TABLE_OPTS = {
    1: dict(widths=['20pt', None, '52pt', '92pt']),
    5: dict(widths=['52pt', None, None, None]),
    6: dict(widths=['92pt', None, '70pt', '80pt']),
    7: dict(widths=['92pt', '52pt', None], hl_rows=(4,)),
    10: dict(widths=['50%', '50%']),
    11: dict(widths=['92pt', None, None, None, None, None, None]),
}

while bi < len(blocks):
    t, p = blocks[bi]
    if state['kh'] > 0:
        state['kh'] -= 1
        if state['kh'] == 0:
            W('</div>')
    if t == 'h1':
        close_chapter()
        state['part'] += 1
        e = [x for x in TOC if x['kind'] == 'part' and x['n'] == state['part']][0]
        W('<section class="fullpage divider" id="%s">' % e['id'])
        W('  <div class="inner"><span class="accent-bar"></span><p class="pn">Part %d</p><h1>%s</h1><p class="pd">%s</p></div>' % (e['n'], esc(e['title']), inl(e['desc'])))
        # chapter list for this part
        idx = TOC.index(e)
        chs = []
        for x in TOC[idx + 1:]:
            if x['kind'] == 'part': break
            chs.append(x)
        W('  <ul class="chapters">' + ''.join('<li><span class="n">%s</span><span><a href="#%s">%s</a></span><span class="pg">%s</span></li>' % (x['n'], x['id'], esc(x['title']), pg(x['id'])) for x in chs) + '</ul>')
        W('</section>')
        bi += 1; continue
    if t == 'h2':
        close_chapter()
        cid = chapter_id(p)
        cls = 'chapter'
        if p == 'Summary': cls += ' first'; cid = 'executive-summary'
        m = re.match(r'(\d+)\. (.*)', p)
        if m: cls += ' conc'
        if cid in RUNON: cls += ' runon'
        state['in_chapter'] = True; state['chapter'] = p
        state['in_sources'] = (p == 'Sources')
        W('<section class="%s" id="%s">' % (cls, cid))
        W('<h2>%s</h2>' % inl(p))
        bi += 1; continue
    if t == 'h3':
        close_figure()
        hm = re.match(r'(What the evidence shows|The reasoning) \((STATED|INFERENCE · [A-Z]+)\)$', p)
        close_kh()
        W('<div class="kh">')
        if hm:
            cls = 'lbl' if hm.group(2) == 'STATED' else 'lbl e'
            W('<h3><span class="%s">%s</span></h3>' % (cls, esc(p)))
        else:
            W('<h3 id="%s">%s</h3>' % (slug(state['chapter'] + '-' + p), inl(p)))
        state['kh'] = 2
        bi += 1; continue
    if t == 'p':
        hm = re.match(r'\*\*((?:What the evidence shows|The reasoning) \((STATED|INFERENCE · [A-Z]+)\))\*\*$', p)
        if hm:
            close_figure(); close_kh()
            W('<div class="kh">')
            W('<h3><span class="%s">%s</span></h3>' % ('lbl' if hm.group(2) == 'STATED' else 'lbl e', esc(hm.group(1))))
            state['kh'] = 2
            bi += 1; continue
        em = re.match(r'\*\*Exhibit (\d+)\. (.*)\*\*$', p)
        if em:
            close_figure()
            no = int(em.group(1)); title = em.group(2)
            seg, nj = take_until_source(bi + 1)
            builder = {2: build_ex2, 3: build_ex3, 4: build_ex4, 8: build_ex8, 9: build_ex9, 12: build_ex12}.get(no)
            keep = no in (2, 3, 4, 5, 6, 7, 9, 10, 11, 12)
            exhibit_open(no, title, ('chart keep' if no in (3, 12) else ('chart' if no == 8 else ('keep' if keep else ''))))
            if builder:
                builder(seg)
            else:
                for tt, pp in seg:
                    if tt == 'table':
                        opts = GENERIC_TABLE_OPTS.get(no, {})
                        W('<div class="tbl-wrap">' + render_table(pp[0], pp[1], **opts) + '</div>')
                    elif tt == 'p' and pp.startswith('Source:'):
                        notes(pp)
                    elif tt == 'p':
                        W('<p class="ex-legend">%s</p>' % inl(pp))
            close_figure()
            bi = nj; continue
        if state['in_sources'] and re.match(r'\*\*(.+)\*\*$', p):
            close_kh()
            W('<div class="kh">')
            W('<h3 id="%s">%s</h3>' % (slug('src-' + p.strip('*')), inl(p.strip('*'))))
            state['kh'] = 2
            bi += 1; continue
        if p.startswith('**WHY IT MATTERS**'):
            rest = p[len('**WHY IT MATTERS**'):].strip()
            W('<p class="lede"><strong>WHY IT MATTERS</strong> %s</p>' % inl(rest))
            bi += 1; continue
        if p.startswith('*What would change this view.*'):
            W('<div class="script"><p>%s</p></div>' % inl(p))
            bi += 1; continue
        if state['chapter'] == 'Summary' and p.startswith('Source:'):
            W('<p class="stats-src">%s</p>' % inl(p))
            bi += 1; continue
        if state['chapter'] == 'Summary' and bi > 0 and blocks[bi - 1][0] == 'h2':
            W('<p class="lede">%s</p>' % inl(p))
            bi += 1; continue
        if re.match(r'\*\*(.+?)\*\*$', p) and blocks[bi + 1][0] == 'table':
            # bold stand-alone line before a table: a table caption (h4)
            close_kh()
            W('<div class="kh">')
            W('<h4>%s</h4>' % inl(p.strip('*')))
            state['kh'] = 2
            bi += 1; continue
        W('<p>%s</p>' % inl(p))
        bi += 1; continue
    if t == 'table':
        header, data = p
        if state['chapter'] == 'Summary' and len(data) == 1 and all(len(h) <= 4 for h in header):
            W(stats_row(header, data))
            bi += 1; continue
        if state['in_sources']:
            def hook_src(ri, ci, v, content, classes):
                if ci == 0:
                    return '<span id="%s">%s</span>' % (v, v), ['first', 'tag']
                return content, classes
            W('<div class="tbl-wrap">' + render_table(header, data, cls='src-tbl', widths=['26pt', '218pt', None], cell_hook=hook_src, tags=False) + '</div>')
            bi += 1; continue
        if header == ['', '']:
            W('<div class="tbl-wrap">' + render_table(header, data, widths=['88pt', None], no_thead=True) + '</div>')
            bi += 1; continue
        if header[0] == 'Flag':
            def hook_flag(ri, ci, v, content, classes):
                if ci == 0:
                    lab = v.strip('*')
                    cls = 'lbl' if lab == 'STATED' else 'lbl e'
                    return '<span class="%s"><strong>%s</strong></span>' % (cls, esc(lab)), ['first']
                return content, classes
            W('<div class="tbl-wrap">' + render_table(header, data, widths=['120pt', None], cell_hook=hook_flag) + '</div>')
            bi += 1; continue
        w = ['120pt', None] if header[0] in ('Term', 'Question') else None
        if header[0] == 'Question': w = ['160pt', None]
        W('<div class="tbl-wrap">' + render_table(header, data, widths=w) + '</div>')
        bi += 1; continue
    if t == 'ul':
        W('<ul class="labs">' if any(lbl_text(x) for x in p) else '<ul>')
        for it in p:
            lt = lbl_text(it)
            W('<li class="lab">%s</li>' % lt if lt else '<li>%s</li>' % inl(it))
        W('</ul>')
        bi += 1; continue
    if t == 'ol':
        W('<ol>')
        for it in p:
            W('<li>%s</li>' % inl(it))
        W('</ol>')
        bi += 1; continue
    raise SystemExit('unhandled block %r' % (blocks[bi],))

close_chapter()

# ------------------------------------------------------------------ back page
W('''<section class="fullpage back">
  <div class="inner">
    <span class="accent-bar"></span>
    <h2>About this document</h2>
    <p>%s</p>
    <p>Facts are as of October 18, 2026, with the V8 revision dated October 19, 2026, unless a table gives another date. The evidence comes from the AladdinSDK core package and the 11 API add-ons published on PyPI, read without being installed or run, and from BlackRock’s public pages, press releases, job postings, talks and podcasts. Every source is listed on the sources sheet in the Reference part; the small S tags throughout the report point to it. A black square marks a claim the files state; an orange square marks an inference, rated by confidence.</p>
    <p>BlackRock and Aladdin are registered trademarks of BlackRock, Inc. Other company and product names are the property of their owners.</p>
    <p>Set in Barlow and Barlow Condensed, open-license stand-ins for BlackRock’s licensed BLK Fort typeface.</p>
  </div>
</section>''' % esc(indep_line))
W('</body></html>')

# ------------------------------------------------------------------ assemble
head = open(HEAD_SRC, encoding='utf-8').read().split('\n')[:468]
head_txt = '\n'.join(head)
head_txt = head_txt.replace('<title>Key Findings: Aladdin Studio</title>', '<title>%s</title>' % esc(fm['title']), 1)
extra = '''<style>
/* V8 additions: components the What It Does edition needs that the briefing stylesheet lacks */
.cover h1{font-size:34pt; line-height:39pt}
.cover .meta{color:#BFBFBF}
.cover .parts .pc + .pc{margin-top:4pt}
.toc .part-desc{font-weight:400; font-size:9pt; color:var(--ink-2); margin-left:6pt}
.divider .pd{font-size:14pt; line-height:18pt; color:#BFBFBF; margin:14pt 0 0; max-width:360pt}
.key-grid .key-ex{font-weight:700}
.key-grid .key-ex a{color:#000}
.key-grid > div{grid-template-columns:96pt 1fr}
a.stag{font-family:var(--font-cond); font-weight:700; font-size:7.5pt; color:var(--ink-2); text-decoration:none; white-space:nowrap; margin-left:1pt}
.notes a.stag{font-size:8pt}
.exhibit .notes{break-before:avoid}
.exhibit table tbody tr:last-child{break-after:avoid}
.exhibit .ex-legend{break-before:avoid}
.kh{break-inside:avoid}
.lbl strong{font-weight:700}
ul > li.lab{list-style:none; padding-left:0}
ul > li.lab::before{content:none}
ul.labs{padding-left:0}
td .lbl, th .lbl{white-space:nowrap}
h3 .lbl::before{vertical-align:1pt; width:7pt; height:7pt}
.chapter.conc > h2{font-size:18pt; line-height:22pt}
.lede strong{font-weight:800}
.band{background:var(--tint-yellow); border:1pt solid var(--yellow); padding:6pt 8pt; margin:6pt 0 8pt; font-size:9pt; line-height:10.8pt; break-inside:avoid}
.studio-box{background:var(--tint-yellow); border:1pt solid var(--yellow); padding:8pt 10pt 6pt; margin:4pt 0 10pt; break-inside:avoid}
.studio-box .studio-head{font-size:10pt; line-height:12pt; margin:0 0 6pt}
.studio-box table{background:#fff}
.studio-box td, .studio-box th{padding-left:6pt}
.areas td, .areas th{font-size:8.5pt; line-height:10pt}
table.src-tbl{font-size:8pt; line-height:9.6pt}
table.src-tbl td{padding:2.5pt 6pt 2.5pt 0}
table.src-tbl td.tag{font-family:var(--font-cond); font-weight:700}
.chart-row .side table{font-size:8.5pt; line-height:10pt}
.chart-row .side td{padding:2.6pt 6pt 2.6pt 0}
.chart-row > div:first-child{flex:none}
.exhibit svg.chart{margin:8pt 0 4pt}
.ex-legend strong{font-weight:700}
.script p{font-size:10pt}
.script em{font-weight:700; font-style:normal}
.chapter ul > li .lbl + *{margin-left:0}
td.ctr .step{margin:0}
</style>'''
open(OUT, 'w', encoding='utf-8').write(head_txt + '\n' + extra + '\n' + '\n'.join(out) + '\n')
print('wrote', OUT, 'blocks', len(blocks), 'toc', len(TOC))
