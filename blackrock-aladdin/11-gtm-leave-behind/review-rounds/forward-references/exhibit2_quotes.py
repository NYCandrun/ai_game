import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
pairs=[
("to execute a particular investment decision”</a><sup class=\"fnref\"><a href=\"#s17\">17</a></sup></td>",
 "to execute a particular investment decision”</a> (Order specification)<sup class=\"fnref\"><a href=\"#s17\">17</a></sup></td>"),
("“new what-if model”</a> compares a changed portfolio",
 "“new what-if model”</a> (Explore classroom recording, speaker unnamed) compares a changed portfolio"),
("The specification’s example statuses run", "The Order specification’s example statuses run"),
("client mandate, or internal guideline”</a>; no application is named",
 "client mandate, or internal guideline”</a> (ComplianceRule specification); no application is named"),
("Violations are “generated at time of the compliance breach,” intraday and overnight.",
 "Violations are “generated at time of the compliance breach” (Violation specification), intraday and overnight."),
("it needs to be confirmed with broker”</a><sup class=\"fnref\"><a href=\"#s17\">17</a></sup></td>",
 "it needs to be confirmed with broker”</a> (BrokerConfirmRouting specification)<sup class=\"fnref\"><a href=\"#s17\">17</a></sup></td>"),
("The people who lead Aladdin Accounting describe the run as going <a",
 "David Schneid or Daniel Shannon of Aladdin Accounting, the recording does not say which, describes the run as going <a"),
("Newman: <a href=", "Richard Newman, Studio’s general manager: <a href="),
("Accounting Books of Record (ABOR) holdings”</a><sup class=\"fnref\"><a href=\"#s22\">22</a></sup>",
 "Accounting Books of Record (ABOR) holdings”</a> (Fivetran’s blog)<sup class=\"fnref\"><a href=\"#s22\">22</a></sup>"),
("and a violation’s <a href=\"https://pypi.org/project/asdk_plugin_compliance/\">“underlying positions.”</a><sup class=\"fnref\"><a href=\"#s17\">17</a></sup>",
 "and a violation’s <a href=\"https://pypi.org/project/asdk_plugin_compliance/\">“underlying positions”</a> (Violation specification)<sup class=\"fnref\"><a href=\"#s17\">17</a></sup>"),
("“we are data managers more than anything else”</a><sup class=\"fnref\"><a href=\"#s20\">20</a></sup>",
 "“we are data managers more than anything else”</a> (Schneid or Shannon)<sup class=\"fnref\"><a href=\"#s20\">20</a></sup>"),
("“retrieved from the ledger_a_summary table.”</a><sup class=\"fnref\"><a href=\"#s17\">17</a></sup>",
 "“retrieved from the ledger_a_summary table”</a> (AborLot specification)<sup class=\"fnref\"><a href=\"#s17\">17</a></sup>"),
("“CFOs, they’re controllers, they’re heads of performance”</a><sup class=\"fnref\"><a href=\"#s20\">20</a></sup>",
 "“CFOs, they’re controllers, they’re heads of performance”</a> (Schneid or Shannon)<sup class=\"fnref\"><a href=\"#s20\">20</a></sup>"),
("“generated for various processes at the portfolio/portfolio group level,”</a><sup class=\"fnref\"><a href=\"#s17\">17</a></sup>",
 "“generated for various processes at the portfolio/portfolio group level”</a> (Valuations specification)<sup class=\"fnref\"><a href=\"#s17\">17</a></sup>"),
]
for a,b in pairs:
    assert s.count(a)==1,(s.count(a),a[:70]); s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok',len(pairs))
