# This is a sample Python script.

import pandas as pd
import requests
import numpy
import json
import pprint
import matplotlib

#Chosen breeds for data
breeds= ['golden retriever','bernese mountain dogs','poodle']

#API Import from API Ninjas, provides the url and key for the data
def get_data(breed):
    api_url = 'https://api.api-ninjas.com/v1/dogs?name={}'.format(breed)
    response = requests.get(api_url, headers={'X-Api-Key': 'bcjVWWN400UdC6kbs0ULww==LQSIctnUnKVHazDi'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

#Creates the JSON file, retreive the name of the breed and the shedding of the breed, appends.
for breed in breeds:
    data = json.loads(get_data(breed))
    dog = []
    dog["name"] = data[0]['name']
    dog['shedding'] = data[0]['shedding']
    dog.append(dog)

pprint.pprint(dog)

#Creating the array
dogarray = np.array(dog)

