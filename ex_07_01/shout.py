# fn = input("Enter a file name:")
fn = "mbox-short.txt"
try:
    fl = open(fn)
except:
    print("No this file!")
    quit()
for line in fl:
    if line.startswith('From:'):
        # print(line)
        print(line.rstrip())
