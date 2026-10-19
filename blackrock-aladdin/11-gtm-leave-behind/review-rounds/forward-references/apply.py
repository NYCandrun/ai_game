import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
pairs=[
# 1 page 13 callout + Exhibit 15 cell
("answers the RFP connector question better than an MCP server with a partial catalog would.",
 "answers the connector question buyers now put in RFPs (Finding 4) better than an MCP server with a partial catalog would."),
("It answers the RFP question about connectors.",
 "It answers the connector question in RFPs (Finding 4)."),
# 2 Part 2 kicker
('<section class="chapter finding" id="f1">\n<h2>1. The public record',
 '<section class="chapter finding" id="f1">\n<h2><span class="pn">Part 2</span>1. The public record'),
# 3 + 4 page 2 glosses
("works only inside the Aladdin login, while data providers",
 "works only inside the Aladdin login, through plugins that call Aladdin’s own APIs, while data providers"),
("the new private-markets data arrives through Data Cloud and Explore<sup",
 "the new private-markets data arrives through Data Cloud and Explore, Aladdin’s portfolio app<sup"),
# 5 Exhibit 2 note
("The labels in brackets are each specification’s stability label; Exhibit 5 explains them.",
 "The labels in brackets are each specification’s stability label: alpha is the earliest, then beta, stable and sunset; Exhibit 5 counts them."),
# Janus commits
("Janus Henderson’s commits and 10-K,",
 "Janus Henderson’s code commits to Studio’s SDK and its 10-K,"),
# Preqin page 3
("up 24 percent with Preqin<sup",
 "up 24 percent including Preqin, the private-markets data firm bought in 2025<sup"),
# Exhibit 17 Databricks
("plus the Snowflake and Databricks connectors and how clients build on top.",
 "plus the Snowflake connector and how clients build on top."),
]
for a,b in pairs:
    assert s.count(a)==1,(s.count(a),a[:70])
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok',len(pairs))
