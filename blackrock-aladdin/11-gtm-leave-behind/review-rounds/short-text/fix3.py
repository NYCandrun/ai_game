import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
pairs=[
("Exhibit 14.</span> Of nine providers a Studio buyer compares, only Aladdin has not shipped or announced AI access to its data",
 "Exhibit 14.</span> Of nine providers a Studio buyer compares, eight have announced AI features or AI access to their data; Aladdin has a job advert"),
("Exhibit 8.</span> Five BlackRock executives have defined Studio on the record since 2024",
 "Exhibit 8.</span> Five BlackRock executives have defined Studio on the record"),
("and they do not say in what sequence steps 4 to 6 happen.</p>",
 "and they do not say in what sequence steps 4 to 6 happen. The labels in brackets are each specification’s stability label; Exhibit 5 explains them.</p>"),
]
for a,b in pairs:
    assert s.count(a)==1,(s.count(a),a[:60])
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
