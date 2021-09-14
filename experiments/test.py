import requests, json

url = 'https://gbfs.baywheels.com/gbfs/en/station_status.json'

source = requests.get(url).json()
print(source)

llist = source['data']['stations']

for i in range(len(llist)):
    if llist[i]['station_id'] == '445': 
        print(llist[i])