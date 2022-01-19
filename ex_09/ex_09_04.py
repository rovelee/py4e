
fname = 'mbox-short.txt'
fh = open(fname)
dct = dict()
for line in fh:
    if not line.startswith('From:'):
        continue
    lsl = line.split()
    eml = lsl[1]
    dct[eml] = dct.get(eml,0) + 1
    # print(eml)
    
mst = -1
twd = None
for k,v in dct.items():
    if v > mst :
        mst = v
        twd = k
print(twd,mst)