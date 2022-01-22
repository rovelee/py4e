from distutils.log import info
from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

print('Retrieving', url)
uh = urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

dd = json.loads(data)
print('Count:', len(dd))

sum=0
for d in dd['comments']:
    # print(d['count'])
    sum+=int(d['count'])
print('Sum:',sum)