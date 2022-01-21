from urllib.request import urlopen
from bs4 import BeautifulSoup as bfsp
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

# url='http://py4e-data.dr-chuck.net/comments_42.html'
url='http://py4e-data.dr-chuck.net/comments_1458575.html'
html= urlopen(url,context=ctx).read()
soup = bfsp(html, 'html.parser')

tags = soup('span')
sum = 0
for tag in tags:
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    sum += int(tag.contents[0])
print(sum)