"""Core module of the data workflow."""

from typing import overload

import pandas as pd
import requests

FIELDS = [
    "is_renting",
    "is_returning",
    "num_bikes_available",
    "num_ebikes_available",
    "num_docks_available",
]


@overload
def station_status(station_ids: list) -> pd.DataFrame: ...


@overload
def station_status(station_ids: None = None) -> pd.Series: ...


def station_status(station_ids: list | None = None) -> pd.DataFrame | pd.Series:
    """Retrieve the status of all the stations."""
    url = "https://gbfs.baywheels.com/gbfs/en/station_status.json"
    source = requests.get(url, timeout=100).json()
    status_df = pd.DataFrame(source["data"]["stations"])
    station_ids = station_ids or list(status_df["station_id"].unique())
    return status_df.loc[status_df["station_id"].isin(station_ids)]


def station_information(station_ids=None):
    """Retrieve all the stations information."""
    url = "https://gbfs.baywheels.com/gbfs/en/station_information.json"
    source = requests.get(url, timeout=100).json()
    information_df = pd.DataFrame(source["data"]["stations"])
    station_ids = station_ids or list(information_df["station_id"].unique())
    return information_df.loc[information_df["station_id"].isin(station_ids)]


def get_results(stations):
    """Get resutls from HTTP requests."""
    url = "https://gbfs.baywheels.com/gbfs/en/station_status.json"
    source = requests.get(url, timeout=100).json()
    stations = stations if stations else ["25", "363", "445"]
    stations_info = station_information(stations)

    llist = source["data"]["stations"]
    values = []
    for elem in llist:
        if (st_id := elem["station_id"]) in stations:
            st_name = stations_info.loc[stations_info["station_id"] == st_id, "name"].squeeze()
            values.append({"name": st_name} | {field: elem[field] for field in FIELDS})
    return values
