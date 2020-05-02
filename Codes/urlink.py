from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

#ignores SSL certificate errors
ctx =  ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
tmp = list()
count = 0
for tag in tags:
    x = re.findall('([0-9]+?)<', tag.decode())
    count = count + 1
    for n in x:
        tmp.append(int(n))

print('count', count)
print('sum', sum(tmp))
