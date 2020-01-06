import os

import folium
import geopandas as gpd
import pandas as pd
from decouple import config
from folium.plugins import MarkerCluster

geo = pd.read_excel(os.path.join('data', 'geo.xlsx'))
# geo_comment = pd.read_excel(os.path.join('data', 'geo.xlsx'))

geo_comments1 = geo.loc[geo['comment_class'] == 1, ['y', 'x']]
geo_comments2 = geo.loc[geo['comment_class'] == -1, ['y', 'x']]

API_KEY = config('YANDEX_API_KEY')
locations = gpd.tools.geocode('Moscow, Russia', provider='Yandex', api_key=API_KEY)
loc = locations.geometry[0]

folium_map = folium.Map(location=[loc.y, loc.x])

marker_cluster = MarkerCluster().add_to(folium_map)

for index, row in geo.iterrows():
    folium.Marker(location=[row['y'], row['x']]).add_to(marker_cluster)

# folium_map
