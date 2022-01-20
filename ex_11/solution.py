import re

smpl_data = '../file/regex_sum_42.txt'
actl_data = '../file/regex_sum_1458573.txt'
reg = '[0-9]+'

# fh = open(smpl_data)
fh = open(actl_data)
sum = 0
cnt = 0
for line in fh:
    line = line.rstrip()
    lst = re.findall(reg, line)
    if len(lst) > 0:
        print(lst)
        for ii in lst:
            sum += int(ii)
            cnt += 1
print(cnt, sum)