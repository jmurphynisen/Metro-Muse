# Metro-Muse

![alt text](https://github.com/jmurphynisen/Metro-Muse/blob/main/Screenshot%20(27).png)

This is a repository for my project, Metro Muse. 
In order to have current functionality, download main.py, MapClass.py, and master.csv

In order to run desktop version, have PyQt installed.
If you cannot see map, I have uploaded reference map with all initial data as an html, "MyMap.html".

**Overview**:
  In this porject, my goal was to be able to visualize user sbumited data as well as data from NY Open Data on a Folium Map in order to provide insight on where musicians can go play to get the most amount of audience members as well as inform avid live music lovers as to where they can find these musicians. For this project I mainly used the NY Open Data Bi-Annual Pedestrian Count to test the program, but I also generated my own data. In order to store and organize this data, I used Pandas to keep track of each report, where each report has an associated coordinate, genre, audience level, and time it was instanciated. Then, to visualize, I used Folium to display each report as a marker, and PyQt to allow users to input their own sightings of musicians. 
  
**Data**:
  The initial data set from NY Open Data has a variety of attributes to pull from, including coordinates and address. I used the coordinates and borough, though I ended up not finding a use for the later. I then parsed and cleaned up the data I took from the initial dataset and put it into a master CSV file, which has columns for coordinates, genre, audience level, and time a report was made. The data from the pedestrian count was made with default values, that being the audience level set to "Medium", time being "00:00:00", and genre being "N/A".
  
**Techniques**:
  I first set up the GUI with text fields for coordinates, genre, and audiences level, as well as a submit button and a window for the Folium map. When the PyQt window is intialized, it populates the map with markers via the master CSV file, which is read in as a dataframe. In order for the user to get the coordinates of where they saw a busker they wanted to report, they can use the MousePosition funct ion which displays in the top right of the map and can copy from there, and input the genre and audience level. Once the submit button is pressed, the input is added as a marker onto the map, appended to the master dataframe, and the map is re-initialized to show the new report.
  
**Citations**:
  https://data.cityofnewyork.us/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h
