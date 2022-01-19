fname = 'mbox-short.txt'
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From:'):
        continue
    lsl = line.split()
    eml = lsl[1]
    print(eml)
    count = count + 1
print('There were %d lines in the file with From as the first word'%count)
