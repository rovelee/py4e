import re

fh = open('../file/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    # x = re.findall('\S+@\S+', line)
    # x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-zZ]', line)
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-zZ]', line)
    if len(x) > 0:
        print(x)
