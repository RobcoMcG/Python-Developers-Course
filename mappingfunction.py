import folium
###Import Pandas

#data = pandas.read_csv("CSV file name.csv")
#Lat = list(data["LATITUDE"])
#Long = list(data["LONGITUDE"])
#

#Mapbox Bright
map = folium.Map(location=[34.9, -78.9], zoom_start=6, tiles="OpenStreetMap")

fgp = folium.FeatureGroup(name="Places")

#for lat,lon in zip(lat, lon):
#fg.add_child(folium.Market(location=[lat, lon], popup="Location Name", icon=folium.Icon(color='green')))

for coordinates in [[34.9, -78.9],[35.9, -79.9]]:
    fgp.add_child(folium.Marker(location=coordinates, popup="Hope Mills, NC", icon=folium.Icon(color='green')))

fgpop = folium.FeatureGroup(name="Population")

fgpop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgpop)

map.add_child(folium.LayerControl())

map.save("Map1.html")
