"""
John Murphy
Metro Muse

This is the Map Class where folium map functionality such as adding markers and creating clusters is stored
TODO: Make function that clusters markers
"""
import folium
from folium.plugins import MarkerCluster
import time
import pandas as pd

global master
master = pd.read_csv('master.csv')

def addReport(genre, borough, alevel):
    t = time.strftime("%H:%M:%S", time.localtime())
    master.append([{'Genre': genre}, {'Borough': borough}, {'aLevel': alevel}, {'Time': t}])

def addMarker(map, lat, lon, level, t, genre):
    popup = t + ", " + genre
    if(level == 'Low'):
        folium.CircleMarker(
            popup=popup,
            location = [lat, lon],
            radius = 10,
            draggable = True,
            fill=True,
            color = 'green'
        ).add_to(map)

    elif(level == 'Medium'):
        folium.CircleMarker(
            popup=popup,
            location = [lat, lon],
            radius = 10,
            draggable = True,
            fill=True,
            color = 'yellow'
        ).add_to(map)

    else:
        folium.CircleMarker(
            popup=popup,
            location = [lat, lon],
            radius = 10,
            draggable = True,
            color = 'red'
        ).add_to(map)  

def initializeMarkers(map):
    for i in range(0, len(master)):
        t = time.strftime("%H:%M:%S", time.localtime())
        addMarker(map, master.iloc[i]['Lat'], master.iloc[i]['Lon'], 'Medium', t, 'Unknown')  
"""
def makeClusters(map, gdf, popupList):
    #Create empty lists to contain the point coordinates and the point pop-up information
    coords, popups = [], [] 
    #Loop through each record in the GeoDataFrame
    for i, row in gdf.iterrows():
        #Append lat and long coordinates to "coords" list
        coords.append([row.geometry.y, row.geometry.x])
        #Create a string of HTML code used in the IFrame popup
        #Join together the fields in "popup_field_list" with a linebreak between them
        label = '<br>'.join([row[field] for field in popupList])
        #Append an IFrame that uses the HTML string to the "popups" list 
        popups.append(folium.element.IFrame(label, width = 300, height = 100))
       #Create a Folium feature group for this layer, since we will be displaying multiple layers
    pt_lyr = folium.FeatureGroup(name = 'pt_lyr')
    
    #Add the clustered points of crime locations and popups to this layer
    pt_lyr.add_children(MarkerCluster(locations = coords, popups = popups))
    
    #Add this point layer to the map object
    map.add_children(pt_lyr)
    return map
"""
