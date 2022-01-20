import re

iptreg = input('Enter a regular expression: ')
try:
    fh = open('../file/mbox.txt')
except:
    print('File dont exist.')
    quit()

cnt = 0
for line in fh:
    line = line.rstrip()
    x = re.findall(iptreg, line)
    if len(x) > 0: cnt += 1
        # print(x)
print('mbox.txt had %d lines that matched %s'%(cnt,iptreg))