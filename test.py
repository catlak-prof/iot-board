import requests
import json
import random
import pprint
import time


headers = {'Content-type': 'application/json'}

url = 'http://127.0.0.1:8000/data/'

data={
    'author': '3',
    'alan1': 34,
    'alan2': 12,
    'alan3': 13,
    'alan4': 14,
    'alan5': 11,
    'alan6': 15,
    'alan7': 16,
    'alan8': 17,


    }

data_json = json.dumps(data)

response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())