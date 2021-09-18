"""Test module for the data.core"""
import pandas as pd
import src.data.core as dc


def test_station_information():
    """Testing the station_information function"""
    information_df = dc.station_information()
    assert isinstance(information_df, pd.DataFrame)


def test_station_status():
    """Testing the station_status function"""
    status_df = dc.station_status()
    status_select_df = dc.station_status(['445', '363', '25'])
    assert isinstance(status_df, pd.DataFrame)
    assert isinstance(status_select_df, pd.DataFrame)
