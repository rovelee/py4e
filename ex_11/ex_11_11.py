import re

fh = open('../file/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    # 在正则表达式中可以用'('和')'选择要匹配的子字符串
    x = re.findall('^X\S*: ([0-9.]+)',line)
    if len(x) > 0:
        print(x)
