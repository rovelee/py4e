# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
fname = 'mbox-short.txt'
fh = open(fname)
cc = 0
fv = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    try:
        fv += float(line.split(' ')[1])
    except:
        print("line:",cc," is not float")
        quit()
    cc = cc+1
print(fv/cc)
# print("Done")