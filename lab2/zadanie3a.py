import folium 
map = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=4, control_scale=True, prefer_canvas=True)
folium.TileLayer('Stamen Terrain', attr='Map data © OpenStreetMap contributors').add_to(map)
folium.Marker([50.04904416612195, 21.981755242425898], popup='uczelnia').add_to(map)
folium.Marker([50.04904416612195, 21.981755242425898], popup='WSIIZ Rzeszów').add_to(map)
folium.Marker([55.69296400027125, 12.599275399999998], popup='Pomnik Mała syrenka w Kopenhaga').add_to(map)
folium.Marker([49.94956953274273, 22.05961809697593], popup='WSIIZ Kielnarowa').add_to(map)
folium.Marker([50.01786019831364, 22.01524968163682], popup='Przystanek Powstańców warszawy 12 Rzeszów').add_to(map)
map.save("Map3a.html")