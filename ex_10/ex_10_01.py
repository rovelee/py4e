fname = input('Enter File: ')
prefix='../file/'
if len(fname)<1 : fname = prefix+'mbox-short.txt'
else: fname = prefix+fname
fh = open(fname)

di = dict()
for lin in fh:
    if not lin.startswith('From:'):
        continue
    lsl = lin.split()
    eml = lsl[1]
    # print(lin)
    di[eml] = di.get(eml,0) + 1
# print(di)

lst = list()

for k,v in di.items():
    lst.append((v,k))

lst.sort(reverse=True)

print(lst[0][1],lst[0][0])