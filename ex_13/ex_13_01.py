from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

print('Retrieving', url)
uh = urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print('Count:', len(counts))

sum = 0
for item in counts:
    # print(item.text)
    sum += int(item.text)

print(sum)

