"""
John Murphy
Metro Muse

This is the main file for the web application, where the barebones functionality is.
TODO: Fuse with template and get lat and lons from master to initialize map with markers, as well as find the middle of a cluster
"""

import time
import pandas as pd
from pandas.core.frame import DataFrame
#import geopandas as gpd
import shapely
from shapely.geometry import Point
import folium
from folium.plugins import MarkerCluster
#from folium.elements import IFrame

master = pd.read_csv('master.csv')
m = folium.Map(location=[40.767937,-73.982155], zoom_start=13)
#folium.TileLayer('Mapbox Control Room').add_to(map)

def addReport(genre, borough, alevel):
    t = time.strftime("%H:%M:%S", time.localtime())
    master.append([{'Genre': genre}, {'Borough': borough}, {'aLevel': alevel}, {'Time': t}])

def addMarker(map, lat, lon, genre, level, t):
    pup = genre + ", " + t
    if(level == 'Low'):
        folium.CircleMarker(
            popup=pup,
            location = [lat, lon],
            radius = 10,
            draggable = True,
            color = 'green'
        ).add_to(map)

    elif(level == 'Medium'):
        folium.CircleMarker(
            popup=pup,
            location = [lat, lon],
            radius = 10,
            draggable = True,
            color = 'yellow'
        ).add_to(map)

    else:
        folium.CircleMarker(
            popup=pup,
            location = [lat, lon],
            radius = 50,
            draggable = True,
            color = 'red'
        ).add_to(map)  

def initializeMarkers():
    for i in range(0, len(master)):
        t = time.strftime("%H:%M:%S", time.localtime())
        addMarker(m, master.iloc[i]['Lat'], master.iloc[i]['Lon'], master.iloc[i]['Genre'], 'Medium', t)

if(__name__ == "__main__"):
    initializeMarkers()
    
