import os

import folium
import geopandas as gpd
import pandas as pd
from decouple import config

geo = pd.read_excel(os.path.join('data', 'geo.xlsx'))
# geo_comment = pd.read_excel(os.path.join('data', 'geo.xlsx'))

API_KEY = config('YANDEX_API_KEY')
locations = gpd.tools.geocode('Moscow, Russia', provider='Yandex', api_key=API_KEY)
loc = locations.geometry[0]

folium_map = folium.Map(location=[loc.y, loc.x])

for index, row in geo.iterrows():
    row['x'], row['y']
    break

folium_map
