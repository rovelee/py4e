fname = input('Enter File: ')
if len(fname)<1 : fname = 'clown.txt'
fh = open(fname)

di = dict()
for lin in fh:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # # print(w)
        # if w in di:
        #     di[w] = di[w] + 1
        #     # print('**EXISTING**')
        # else:
        #     di[w] = 1
        #     # print('***NEW***')
        # print(di[w])
        di[w] = di.get(w,0) + 1
# print(di)

largest = -1
theword = None
for k,v in di.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k

print('The most word:',theword,largest)
