import requests

FIELDS = ['station_id', 'is_renting', 'num_bikes_available', 'num_ebikes_available']

def get_results():
    url = 'https://gbfs.baywheels.com/gbfs/en/station_status.json'
    source = requests.get(url).json()

    llist = source['data']['stations']

    values = []
    for i in range(len(llist)):
        if (llist[i]['station_id'] == '445' 
            or llist[i]['station_id'] == "25"
            or llist[i]['station_id'] == "363"): 
            values.append({field: llist[i][field] for field in FIELDS})
    return values