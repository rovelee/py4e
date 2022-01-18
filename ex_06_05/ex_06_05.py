str = 'X-DSPAM-Confidence: 0.8475'
# print(str)
ipos=str.find(':')
# print(ipos)
peice=str[ipos+1:]
# print(peice)
value=float(peice)
print(value)
