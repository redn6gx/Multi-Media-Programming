import requests, json
from pprint import pprint

# agify.io
# This api does not require an api key to use.
# The api predicts the age of a person based off of a name.

endpoint = 'https://api.agify.io?name=bobby'    # api url with the name you want to pass to api call

try:
  r = requests.get(endpoint)     # attempt api call
  data = r.json()   # save json object
  pprint(data)  # use pretty print to print retrieved json object
except:
  print('please try again')

if data:
    for item in data: # iterate through each field in json object
        print(f'{item}: {data[item]}')  # print field name and value
else:
    print('no data')
    