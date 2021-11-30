"""
John Murphy
Metro Muse

This script generates the master csv file used to store all data from, 
NYCOpenData bi-annual foot traffic csv and user reports.

TODO: Convert coordinates to string to extract long lat.
"""
import pandas as pd
import re

def extractLatLon(row):
    pieces = re.search(r'\((.*) (.*)\)',row)
    print(pieces.group(1), pieces.group(2))
    return(float(pieces.group(1)),float(pieces.group(2)))

nyDF = pd.read_csv('PedCountLocationsMay2015.csv')
df = pd.DataFrame(columns=["Genre", "Coordinates", "Borough", "aLevel", "Time"])

#initialize columns
df['Coordinates'] = nyDF['the_geom']
df['Borough'] = nyDF['Borough']
df['Genre'] = 'N/A'
df['aLevel'] = 'Medium'
df["Time"] = '00:00:00'

df.to_csv('master.csv', index=False)
