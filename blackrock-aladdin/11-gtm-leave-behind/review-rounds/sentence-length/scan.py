import re, sys
from html.parser import HTMLParser
path = sys.argv[1]
html = open(path, encoding="utf-8").read()
BLOCK = {"p","td","th","li","div","h1","h2","h3","h4","h5","figcaption","caption","blockquote","dt","dd","section","table","tr","ul","ol","body","br"}
class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0  # depth of skipped elements
        self.stack = []
        self.units = []  # (line, context, text)
        self.cur = []
        self.cur_line = None
        self.in_source = False
        self.ctx = ""
        self.drop_a = False
    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        if t:
            self.units.append((self.cur_line, self.ctx, t))
        self.cur = []; self.cur_line = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.stack.append(tag)
        if tag in ("style","script","head","svg","sup","title"):
            self.skip += 1
        if tag in BLOCK:
            self.flush()
            if a.get("id"): self.ctx = a["id"]
            elif a.get("class"): self.ctx = tag + "." + a["class"]
            if tag == "p" and re.fullmatch(r"s\d+", a.get("id","")):
                self.in_source = True
        if self.in_source and tag == "span" and a.get("class") == "t":
            self.skip += 1; self.stack[-1] = "span.t"
        if tag == "a" and self.in_source:
            self.drop_a = True
    def handle_endtag(self, tag):
        # pop to matching
        while self.stack:
            t = self.stack.pop()
            if t in ("style","script","head","svg","sup","title","span.t"):
                self.skip -= 1
            if t == "a": self.drop_a = False
            if t == tag or (t == "span.t" and tag == "span"):
                break
        if tag in BLOCK:
            self.flush()
            if tag == "p": self.in_source = False
    def handle_data(self, d):
        if self.skip: return
        if self.drop_a and d.strip().startswith("http"): return
        if self.cur_line is None: self.cur_line = self.getpos()[0]
        self.cur.append(d)
p = P(); p.feed(html); p.flush()

ABBR = ["vs.", "No.", "Inc.", "Mr.", "Ms.", "Dr.", "e.g.", "i.e.", "St.", "Jr.", "Ltd.", "Corp.", "cf.", "approx.", "Co."]
def split_sentences(t):
    s = t
    for i,a in enumerate(ABBR):
        s = s.replace(a, a[:-1] + "\x00")
    s = s.replace("...", "\x00\x00\x00").replace("…", "\x01")
    # boundary: terminal punct, optional closing quotes/parens, whitespace, then any start
    parts = re.split(r"(?:(?<=[.!?][”’\)\]\"'])|(?<=[.!?]))\s+(?=[\"“‘(\[A-Za-z0-9–—$€£])", s)
    parts2 = []
    for x in parts:
        parts2.append(x.replace("\x00", ".").replace("\x01", "…"))
    return parts2

def wc(s):
    return len(s.split())

out = []
for line, ctx, t in p.units:
    for s in split_sentences(t):
        n = wc(s)
        if n >= 30:
            out.append((line, ctx, n, s))
print(f"units={len(p.units)}")
for line, ctx, n, s in out:
    print(f"\nLINE {line} [{ctx}] {n} words:\n  {s}")
print(f"\nTOTAL >=30: {len(out)}")
if "--all" in sys.argv:
    for line, ctx, t in p.units:
        for s in split_sentences(t):
            n = wc(s)
            if n >= 25: print(f"{n:3d} L{line} [{ctx}] {s[:110]}")
