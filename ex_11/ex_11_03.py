import re

fh = open('../file/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    if re.search('F..m:',line):
        print(line)
