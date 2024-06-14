import folium

# Tworzenie mapy wycentrowanej na określonej lokalizacji z poziomem powiększenia 17 przy użyciu kafelków Stamen Terrain z odpowiednią atrybucją
mapa = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=17,)

# Lista lokalizacji do dodania wskaźników
lokalizacje = [
    {"location": [50.04904416612195, 21.981755242425898], "popup": "Pierwszy wskaźnik"},
    {"location": [50.04984416612195, 21.982755242425898], "popup": "Drugi wskaźnik"},
    {"location": [50.04824416612195, 21.980755242425898], "popup": "Trzeci wskaźnik"},
]

# Dodanie wskaźników na mapę
for miejsce in lokalizacje:
    marker = folium.Marker(
        location=miejsce["location"],
        popup=miejsce["popup"],
        icon=folium.Icon(icon='info-sign')
    )
    marker.add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("Map5.html")
