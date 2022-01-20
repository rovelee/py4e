from math import floor
import re

prefix = '../file/'
fnm = input('Enter file:')
try:
    fhd = open(prefix+fnm)
except:
    print('File open failed!')
    quit()

sum = 0
cnt = 0
for line in fhd:
    line = line.rstrip()
    rvs = re.findall('New Revision: ([0-9]+)', line)
    if len(rvs) > 0:
        sum += int(rvs[0])
        cnt += 1
print(floor(sum/cnt))