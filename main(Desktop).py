"""
John Murphy
Metro Muse

this main file is for desktop functionality, hence the gui elements and use of PyQt.
for website version, go to main(Website)
TODO: 
"""
import re
import io
import sys
import time
import folium
import MapClass
import pandas as pd
import requests
from geopy.extra.rate_limiter import RateLimiter
from geopy import Nominatim
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel, QVBoxLayout


class Window(QtWidgets.QMainWindow):
    master = pd.read_csv('master.csv')
    m = folium.Map(
        title='NYC',
        location=(40.767937,-73.982155), 
        zoom_start=13
        )
    geocoder = 'http://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self):
        super().__init__()
        self.initWindow()
        layout = QVBoxLayout()
        self.setLayout(layout)
        #create map and fill with markers from NYC Open Data

        data = io.BytesIO()
        self.m.save(data, close_file=False)

        #self.view.setHtml(data.getvalue().decode())
        webView = QtWebEngineWidgets.QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

    def initWindow(self):
        self.setWindowTitle(self.tr("MAP PROJECT"))
        self.setFixedSize(1500, 800)
        self.buttonUI()

    def buttonUI(self):
        buttonList = []
        textBoxList = []

        #initialize elements
        submitButton = QtWidgets.QPushButton(self.tr("Submit"))
        buttonList.append(submitButton)

        self.locationTextBox = QLineEdit(self)
        self.locationTextBox.setPlaceholderText("Enter Location")
        self.genreTextBox = QLineEdit(self)
        self.genreTextBox.setPlaceholderText("Enter Genre")
        self.levelTextBox = QLineEdit(self)
        self.levelTextBox.setPlaceholderText("Enter Audience Level")
        textBoxList.extend((self.locationTextBox, self.genreTextBox, self.levelTextBox))

        #configure size
        for x in buttonList: x.setFixedSize(50, 20)
        for x in textBoxList: x.resize(120, 5)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setContentsMargins(50, 50, 50, 50)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)

        button_container = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(button_container)
        vlay.setSpacing(5)
        vlay.addStretch()

        #add to overlay
        for x in textBoxList: vlay.addWidget(x)

        vlay.addWidget(submitButton)
        vlay.addStretch()
        lay.addWidget(button_container)
        lay.addWidget(self.view, stretch=1)
        submitButton.clicked.connect(self.onClick)

    def onClick(self):
        t = time.strftime("%H:%M:%S", time.localtime())
        locationValue = self.locationTextBox.text()
        genreValue = self.genreTextBox.text()
        levelValue = self.levelTextBox.text()
        print(levelValue)
        coords = re.findall("\d+\.\d+", locationValue)
        MapClass.addMarker(self.m, coords[0], coords[1], levelValue, t)
        newRow = {'Genre': genreValue, 'Lon': coords[1], 'Lat': coords[0], 'Borough': 'N/A', 'aLevel': levelValue, 'Time': t}
        self.master.append(newRow, ignore_index=True)
        self.master.to_csv('temp.csv')
"""
        requestCoord = requests.get(self.geocoder, params=locationValue)
        request = requestCoord.json()['results']
        coords = request[0]['geometry']['location']
        MapClass.addMarker(self.m, coords['lng'], coords['lat'], levelValue, t)
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('window closed')
