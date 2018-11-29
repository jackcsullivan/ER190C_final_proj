import pandas as pd
import requests

def get_epoch(timestamp_str, tz='US/Pacific'):
    ts = pd.Timestamp(timestamp_str,  tz=tz)
    return int(ts.value / (1*10**9))

def get_hourly_weather(lat, lon, timestamp_str, tz='US/Pacific', key='c75fe89710b37b9fd1531010a8968ef1'):
    base_url = 'https://api.darksky.net/forecast/' + key + '/'
    with_location = base_url + str(lat) + ',' + str(lon)
    epoch = get_epoch(timestamp_str, tz)
    with_time = with_location + ',' + str(epoch)
    resp = requests.get(with_time)
    if resp.status_code != 200:
        raise RuntimeError('API call errored with code: ' + resp.status_code)
    data_dict = resp.json()
    daterange = pd.date_range(timestamp_str, periods=24, freq='1H')
    df = pd.DataFrame(data_dict['hourly']['data'])
    df.index = daterange
    df = df.drop(columns=['time'])
    return df