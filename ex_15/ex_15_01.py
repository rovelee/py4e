import sqlite3

conn=sqlite3.connect('assignment')
cur=conn.cursor()

sql = '''
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER);
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Daryl', 16);
INSERT INTO Ages (name, age) VALUES ('Aleksandr', 16);
INSERT INTO Ages (name, age) VALUES ('Faria', 20);
INSERT INTO Ages (name, age) VALUES ('Sydnee', 36);'''

cur.executescript(sql)
conn.commit()

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for res in cur:
    print(res)

cur.close()
conn.close()