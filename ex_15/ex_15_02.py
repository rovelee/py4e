import sqlite3
import re
from sys import prefix

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

prefix='../file/'
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'

fh = open(prefix+fname)
dct=dict()

for line in fh:
    line=line.rstrip()
    lst=re.findall('^From: .+@(.+)',line)
    if len(lst)>0:
        dct[lst[0]]=dct.get(lst[0],0)+1

for k,v in dct.items():
    cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, ?)''',(k,v))

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

conn.commit()
cur.close()
