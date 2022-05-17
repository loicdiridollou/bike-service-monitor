"""Core module of the data workflow."""
import requests
import pandas as pd


FIELDS = ['is_renting', 'is_returning',
          'num_bikes_available', 'num_ebikes_available', 'num_docks_available']


def station_status(station_ids=None):
    """Retrieve the status of all the stations"""
    url = 'https://gbfs.baywheels.com/gbfs/en/station_status.json'
    source = requests.get(url).json()
    status_df = pd.DataFrame(source['data']['stations'])
    station_ids = station_ids if station_ids else status_df['station_id'].unique()
    return status_df.loc[status_df['station_id'].isin(station_ids)]


def station_information(station_ids=None):
    """Retrieve all the stations information"""
    url = 'https://gbfs.baywheels.com/gbfs/en/station_information.json'
    source = requests.get(url).json()
    information_df = pd.DataFrame(source['data']['stations'])
    station_ids = station_ids if station_ids else information_df['station_id'].unique()
    return information_df.loc[information_df['station_id'].isin(station_ids)]


def get_results(stations):
    """Temporary function"""
    url = 'https://gbfs.baywheels.com/gbfs/en/station_status.json'
    source = requests.get(url).json()
    stations = stations if stations else ['25', '363', '445']
    stations_info = station_information(stations)

    llist = source['data']['stations']
    values = []
    import pdb; pdb.set_trace()
    for elem in llist:
        if (st_id := elem['station_id']) in stations:
            res = {'name': stations_info.loc[stations_info['station_id'] == st_id, 'name'].squeeze()}
            values.append(res | {field: elem[field] for field in FIELDS})
    return values
