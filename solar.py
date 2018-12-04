import pysolar.solar as ps
import datetime
import pytz
import pandas as pd

def get_clear_sky_radiation(lat, lon, timestamp_str, tz):
    dt = pd.to_datetime(timestamp_str)
    tz_aware = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, 0, pytz.timezone('US/Eastern'))
    altitude = ps.get_altitude(lat, lon, tz_aware)
    watts_per_sq_meter = ps.radiation.get_radiation_direct(tz_aware, altitude)
    return watts_per_sq_meter