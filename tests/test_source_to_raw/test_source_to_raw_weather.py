from ./project.gangs_of_new_pork.src.source_to_raw.source_to_raw_weather import download_csvs_from_endpoint

#import pytest

def test_download_csvs_from_endpoint():
    #arrange
    STATION_IDS = [
        "USC00284339",
        "USC00287545",]

    BASE_ENDPOINT = "https://www.ncei.noaa.gov/access/past-weather/ID/data.csv"
    #act
    result = download_csvs_from_endpoint(BASE_ENDPOINT, STATION_IDS)
    #assert
    assert isinstance(result, list) 
    assert len(result) > 0
