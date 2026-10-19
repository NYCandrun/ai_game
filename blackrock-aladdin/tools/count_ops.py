import json, glob, re, sys, collections
root = sys.argv[1]
files = sorted(glob.glob(root + "/**/swagger.json", recursive=True))
tot=0; linter=0; citizen=0; scoped=0; rw=collections.Counter(); lro=0; dep=0; batch=0; filt=0; search=0
per_pkg = collections.defaultdict(lambda: collections.Counter())
citizen_ops=[]
for f in files:
    pkg = f.split('/')[len(root.rstrip('/').split('/'))].split('-')[0]
    d = json.load(open(f))
    secdefs = d.get('securityDefinitions', {})
    for path, ops in d.get('paths', {}).items():
        for m, op in ops.items():
            if m.lower() not in ('get','post','put','patch','delete'): continue
            tot+=1; per_pkg[pkg]['ops']+=1
            txt = (op.get('summary','') + ' ' + op.get('description','') + ' ' + json.dumps(op.get('parameters',[])))
            if 'api-linter' in (op.get('summary','') + ' ' + op.get('description','')): linter+=1; per_pkg[pkg]['linter']+=1
            if 'break all citizen developers' in op.get('description',''): citizen+=1; citizen_ops.append((pkg, d['info'].get('title'), m.upper(), path))
            if op.get('x-aladdin-lro'): lro+=1
            if op.get('deprecated'): dep+=1
            if 'batch' in path.lower(): batch+=1; per_pkg[pkg]['batch']+=1
            if ':filter' in path or ':search' in path: filt+=1; per_pkg[pkg]['filter_search']+=1
            # scopes
            scopes=set()
            for sec in op.get('security', []):
                for k,v in sec.items():
                    for s in v: scopes.add(s)
            kinds=set()
            for s in scopes:
                if s.endswith(':read'): kinds.add('read')
                elif s.endswith(':write'): kinds.add('write')
            if kinds: scoped+=1; rw[tuple(sorted(kinds))]+=1
print("total ops", tot, "| ops with api-linter note", linter, "| ops with citizen note", citizen, "| ops with read/write scope", scoped, dict(rw), "| x-aladdin-lro", lro, "| deprecated", dep, "| batch paths", batch, "| filter/search paths", filt)
for p,c in sorted(per_pkg.items()): print(p, dict(c))
for c in citizen_ops: print("  citizen:", c)
# extension keys used on ops
