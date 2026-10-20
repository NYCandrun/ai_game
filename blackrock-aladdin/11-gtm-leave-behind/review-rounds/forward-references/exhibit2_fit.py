import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
pairs=[
('<table class="path">\n<colgroup><col style="width:62pt"><col style="width:138pt"><col style="width:138pt"><col></colgroup>',
 '<table class="path">\n<colgroup><col style="width:54pt"><col style="width:141pt"><col style="width:141pt"><col></colgroup>'),
("(Order specification)<sup", "(Order spec)<sup"),
("(Explore classroom recording, speaker unnamed) compares", "(Explore classroom recording) compares"),
("(ComplianceRule specification); no application is named", "(ComplianceRule spec); no application is named"),
("(Violation specification), intraday and overnight", "(Violation spec), intraday and overnight"),
("(BrokerConfirmRouting specification)<sup", "(BrokerConfirmRouting spec)<sup"),
("David Schneid or Daniel Shannon of Aladdin Accounting, the recording does not say which, describes the run as going <a",
 "Schneid or Shannon of Aladdin Accounting (the recording does not say which) describes the run as going <a"),
("(Violation specification)<sup", "(Violation spec)<sup"),
("(AborLot specification)<sup", "(AborLot spec)<sup"),
("(Valuations specification)<sup", "(Valuations spec)<sup"),
("the Aladdin Accounting episode<sup class=\"fnref\"><a href=\"#s20\">20</a></sup>; Fivetran",
 "the Aladdin Accounting episode with David Schneid and Daniel Shannon, which does not label who is speaking<sup class=\"fnref\"><a href=\"#s20\">20</a></sup>; Fivetran"),
]
for a,b in pairs:
    assert s.count(a)==1,(s.count(a),a[:70]); s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok',len(pairs))
