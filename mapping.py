import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "OpenStreetMap")
fg = folium.FeatureGroup(name="Volcano Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location = [lt, ln], popup=folium.Popup( "The Height of the volcano is " + str(el) + " m", parse_html=True), icon=folium.Icon(color='blue')))

map.add_child(fg)
map.save("Map1.html")