import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup as bfsp
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
cnt = int(input('Enter count:'))
pos = int(input('Enter position:'))

ii = 0
while ii <= cnt:
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = bfsp(html, 'html.parser')
    tags = soup('a')
    url = tags[pos-1].get('href', None)
    ii += 1
