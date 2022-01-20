import re

fh = open('../file/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)
