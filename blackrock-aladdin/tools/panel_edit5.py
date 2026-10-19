import sys
F = sys.argv[1]
html = open(F, encoding="utf-8").read()
def rep(old, new, count=1):
    global html
    n = html.count(old)
    assert n == count, f"expected {count}, found {n}: {old[:90]!r}"
    html = html.replace(old, new)
rep('<p class="cap">Projected growth in API calls across BlackRock and Aladdin by 2030, the fastest-growing measure on a 2025 Investor Day slide</p>',
    '<p class="cap">Projected growth in API calls by 2030, the fastest-growing measure on a 2025 Investor Day slide</p>')
rep('<div class="method" style="margin-top:4pt">', '<div class="method" style="margin-top:4pt; margin-bottom:6pt">')
rep('<ol style="margin-bottom:8pt; columns:2; column-gap:18pt">', '<ol style="margin-bottom:4pt; columns:2; column-gap:18pt">')
open(F, 'w', encoding='utf-8').write(html)
print('ok')
