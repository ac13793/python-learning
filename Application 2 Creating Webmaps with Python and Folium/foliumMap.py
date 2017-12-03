import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [30.58, -99.09], zoom_start = 6, tiles = "Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
for lt, ln, el in zip(lat, lon, elev):
    # fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) +" m", icon=folium.Icon(color='green')))
    # TO show circle markers
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) +" m", fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+ "m",
    fill_color = color_producer(el), color='grey', fill_opacity=0.7))

map.add_child(fg)
map.save("foliumMap.html")