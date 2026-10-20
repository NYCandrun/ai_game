import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
pairs=[
('<colgroup><col style="width:54pt"><col style="width:141pt"><col style="width:141pt"><col></colgroup>',
 '<colgroup><col style="width:50pt"><col style="width:142pt"><col style="width:142pt"><col></colgroup>'),
("before anything is traded<sup class=\"fnref\"><a href=\"#s21\">21</a></sup>. The specifications name no order screen<sup class=\"fnref\"><a href=\"#s17\">17</a></sup></td>",
 "before anything is traded<sup class=\"fnref\"><a href=\"#s21\">21</a></sup></td>"),
("Schneid or Shannon of Aladdin Accounting (the recording does not say which) describes", "Schneid or Shannon of Aladdin Accounting describes"),
("(Violation spec), intraday and overnight. A check", "(Violation spec). A check"),
("For each step it records who acts, which product or application BlackRock names, and which of the 54 public API specifications covers the step",
 "For each step it records who acts, which product BlackRock names, and which of the 54 public specifications covers it"),
]
for a,b in pairs:
    assert s.count(a)==1,(s.count(a),a[:70]); s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok',len(pairs))
