import pandas as pd
from typing import Tuple


def convert_to_degrees(lat: str, lon: str) -> Tuple[float, float]:
    split_lat = lat.split(chr(176))
    lat_deg = split_lat[0]
    lat_min, lat_sec = split_lat[1].split("'")
    lat_coord_strs = [lat_deg, lat_min, lat_sec]
    lat_coord = [float(x) for x in lat_coord_strs]
    lat_deg, lat_min, lat_sec = lat_coord

    split_lon = lon.split(chr(176))
    lon_deg = split_lon[0]
    lon_min, lon_sec = split_lon[1].split("'")
    lon_coord_strs = [lon_deg, lon_min, lon_sec]
    lon_coord = [float(x) for x in lon_coord_strs]
    lon_deg, lon_min, lon_sec = lon_coord

    lat_dd = lat_deg + lat_min / 60 + lat_sec / 3600
    lon_dd = lon_deg + lon_min / 60 + lon_sec / 3600

    return lat_dd, lon_dd


df = pd.DataFrame({'latitude': ["2°45'49.0", "8°31'18.8", "8°41'18.8"],
                   'longitude': ["47°29'51.5", "46°44'47.8", "45°42'47.8"]})

df['lat_lon_dd'] = df.apply(lambda row: convert_to_degrees(row['latitude'], row['longitude']), axis=1)

print(df)
