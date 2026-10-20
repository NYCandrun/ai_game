import json,glob,os,collections
J="/root/.claude/projects/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/subagents/workflows"
S="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc"
claims={}
for f in glob.glob(S+"/claims/claims_p*.tsv"):
    for l in open(f):
        p=l.rstrip("\n").split("\t")
        if len(p)>=4: claims[p[0]]={"page":p[1],"loc":p[2],"claim":p[3],"src":p[4] if len(p)>4 else ""}
first={}; second={}
for jf in glob.glob(J+"/*/journal.jsonl"):
    lab={}
    for l in open(jf):
        d=json.loads(l)
        if d.get("type")=="started": lab[d["key"]]=d["label"]
        if d.get("type")=="result" and d.get("result") and isinstance(d["result"],dict):
            L=lab.get(d["key"],"")
            for r in d["result"].get("rows",[]):
                if L.startswith("check "): first[r["id"]]=r
                elif L.startswith("re-check "): second[r["id"]]=r
missing=[i for i in claims if i not in first]
fin={}
for i,r in first.items():
    s=second.get(i)
    fin[i]={"first":r["verdict"],"final":s["final_verdict"] if s else r["verdict"],"agree":(s or {}).get("agrees_with_first"),
            "receipt":(s or r)["receipt"],"first_receipt":r["receipt"],"correction":(s or r)["correction"] or r["correction"],"claim":r.get("claim") or claims.get(i,{}).get("claim","")}
c1=collections.Counter(v["first"] for v in fin.values()); c2=collections.Counter(v["final"] for v in fin.values())
print("claims",len(claims),"checked",len(first),"rechecked",len(second),"missing",len(missing))
print("first:",dict(c1)); print("final:",dict(c2))
json.dump({"fin":fin,"claims":claims,"missing":missing},open(S+"/compiled.json","w"),indent=1)
