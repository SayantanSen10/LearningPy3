from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
file = urlopen(url, context = 'ctx').read()
print('Retrieved', len(file), 'characters')

tree = ET.fromstring(file)
lst = tree.findall('comments/comment')
count = 0
list = list()
for items in lst:
    count = count + 1
    list.append(int(items.find('count').text))

print('Count:', count)
print('Sum:', sum(list))
