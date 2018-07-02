import folium
map = folium.Map(location=[8.998881,7.423228], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[8.998881,7.423228], popup="Hi welcome", icon=folium.Icon(color="red")))
map.add_child(fg)

map.save("map1.html")
