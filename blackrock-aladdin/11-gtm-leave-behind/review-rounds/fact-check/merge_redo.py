import json,glob,collections
J="/root/.claude/projects/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/subagents/workflows"
S="/tmp/claude-0/-home-user-ai-game/44510f87-22a4-5476-9273-389e23c654a8/scratchpad/fc"
d=json.load(open(S+"/compiled.json")); fin=d["fin"]; aff=json.load(open(S+"/redo_ids.json"))
redo={}
for jf in glob.glob(J+"/*/journal.jsonl"):
    lab={}
    for l in open(jf):
        x=json.loads(l)
        if x.get("type")=="started": lab[x["key"]]=x["label"]
        if x.get("type")=="result" and lab.get(x["key"],"").startswith("redo ") and isinstance(x.get("result"),dict):
            for r in x["result"]["rows"]: redo[r["id"]]=r
print("redone",len(redo),"of",len(aff),"missing",[i for i in aff if i not in redo][:10])
ch=collections.Counter(); moves=[]
for i,r in redo.items():
    old=fin[i]["final"]; new=r["new_verdict"]
    if old!=new: moves.append((old,new)); 
    fin[i].update({"pre_redo":old,"final":new,"receipt":r["receipt"],"correction":r["finding"],"redo":True,"redo_searches":r["searches_run"]})
print("changed",len(moves)); print(collections.Counter(moves).most_common())
print("final now:",dict(collections.Counter(v["final"] for v in fin.values())))
json.dump(d,open(S+"/compiled_redo.json","w"),indent=1)
