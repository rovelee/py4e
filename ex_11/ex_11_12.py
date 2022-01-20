import re

fh = open('../file/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print(x)
