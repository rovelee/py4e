import string

fnm = 'romeo-full.txt'
fh = open(fnm)

cnts = dict()
for ln in fh:
    ln = ln.rstrip()
    ln = ln.translate(ln.maketrans('','',string.punctuation))
    ln = ln.lower()
    wds = ln.split()
    for wd in wds:
        cnts[wd] = cnts.get(wd, 0) + 1

print(cnts)