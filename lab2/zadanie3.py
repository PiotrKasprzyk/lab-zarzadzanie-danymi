import folium 
map = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=4, control_scale=True, prefer_canvas=True)
folium.TileLayer('Stamen Terrain', attr='Map data © OpenStreetMap contributors').add_to(map)
folium.Marker([50.04904416612195, 21.981755242425898], popup='uczelnia').add_to(map)
map.save("Map3.html")
