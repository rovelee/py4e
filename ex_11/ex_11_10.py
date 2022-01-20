import re

fh = open('../file/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+',line):
        print(line)
