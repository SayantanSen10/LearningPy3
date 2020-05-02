from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
co = 0
while(co != count):
    co = co + 1
    file = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(file, 'html.parser')

    tags = soup('a')
    po = 0
    for tag in tags:
        po = po + 1
        if po == pos:
            x = tag.get('href', None)
            print('Retrieving: ', x)
            url = x
