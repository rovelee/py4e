
fname = input('Enter File: ')
prefix='../file/'
if len(fname)<1 : fname = prefix+'mbox-short.txt'
else: fname = prefix+fname
fh = open(fname)

dct = dict()
for ln in fh:
    if not ln.startswith('From '):
        continue
    lsl = ln.split()
    tim = lsl[5]
    hour = tim.split(':')[0]
    dct[hour] = dct.get(hour,0) + 1

lst = list(dct.items())
lst.sort()

for (k,v) in lst:
    print(k,v)
