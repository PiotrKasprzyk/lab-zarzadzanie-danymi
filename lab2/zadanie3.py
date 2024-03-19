import folium 
map = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=17, tiles='Stamen Terrain')
folium.Marker([50.04904416612195, 21.981755242425898], popup='uczelnia').add_to(map)
map.save("Map3.html")
