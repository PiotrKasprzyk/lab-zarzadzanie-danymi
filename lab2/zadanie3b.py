import folium 
map = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=17, tiles='Stamen Terrain')
folium.Marker([50.04904416612195, 21.981755242425898], popup='uczelnia',icon=folium.Icon(color='red')).add_to(map)
folium.Marker([50.04904416612195, 21.981755242425898], popup='WSIIZ Rzeszów',icon=folium.Icon(color='green')).add_to(map)
folium.Marker([55.69296400027125, 12.599275399999998], popup='Pomnik Mała syrenka w Kopenhaga',icon=folium.Icon(color='blue')).add_to(map)
folium.Marker([49.94956953274273, 22.05961809697593], popup='WSIIZ Kielnarowa',icon=folium.Icon(color='white')).add_to(map)
folium.Marker([50.01786019831364, 22.01524968163682], popup='Przystanek Powstańców warszawy 12 Rzeszów',icon=folium.Icon(color='yellow')).add_to(map)
map.save("Map3b.html")