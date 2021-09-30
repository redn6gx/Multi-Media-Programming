import requests, json
from pprint import pprint
from PIL import Image

my_key = 'fyxMdzMEfpVRGfl172zO3KnL14zk88iueOsWFcR2'

payload = {
  'api_key': my_key,
  'start_date': '2020-03-09',
  'end_date': '2020-03-11'
}
endpoint = 'https://api.nasa.gov/planetary/apod'
try:
  r = requests.get(endpoint, params=payload)
  data = r.json()
  pprint(data)
except:
  print('please try again')

if data:
    for  item in data:
        if 'hdurl' in item:
            im = Image.open(requests.get(item['hdurl'], stream=True).raw)
            im.show()
        elif 'url' in item:
            print(item['url'])
else:
    print('no data')