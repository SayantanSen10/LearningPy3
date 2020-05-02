import urllib.request, urllib.error, urllib.parse
import json

url = input('Enter URL: ')
file = urllib.request.urlopen(url)
data = file.read().decode()

try:
    js = json.loads(data)
except:
    js = None

cmnts = js['comments']

sum = 0
count = 0
for counts in cmnts:
    i = int(counts['count'])
    sum = sum + i
    count = count + 1

print('Count: ', count)
print('Sum: ', sum)
