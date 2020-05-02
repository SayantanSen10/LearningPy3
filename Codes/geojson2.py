import urllib.request, urllib.error, urllib.parse
import json

api_key = False

if api_key == False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

location = input('Enter location: ')

loc = dict()
loc['address'] = location
loc['key'] = api_key

url = serviceurl + urllib.parse.urlencode(loc)
file = urllib.request.urlopen(url)
data = file.read().decode()

js = json.loads(data)

if not js or 'status' not in js or js['status'] != 'OK':
    print('Failed to retrieve data')
else:
    print(json.dumps(js, indent = 4))

x = js['results'][0]['place_id']
print('Place id:', x)
