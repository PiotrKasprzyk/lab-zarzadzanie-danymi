import folium

# Tworzenie mapy wycentrowanej na określonej lokalizacji z poziomem powiększenia 17 przy użyciu kafelków Stamen Terrain z odpowiednią atrybucją
mapa = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=17, )

# Dodanie wskaźnika (markera) na mapę
marker = folium.Marker(
    location=[50.04904416612195, 21.981755242425898],
    popup='Tutaj jest wskaźnik',
    icon=folium.Icon(icon='info-sign')
)
marker.add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("Map4.html")
