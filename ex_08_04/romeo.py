fname= 'romeo.txt'
fh = open(fname)
slist = []
for line in fh:
    lsl = line.split()
    for str in lsl:
        if str not in slist:
            slist.append(str)   

slist.sort()
print(slist)
