import folium
import pandas as pd

# Wczytanie danych z pliku volcanoes.txt
data = pd.read_csv('volcanoes.txt')

# Tworzenie mapy wycentrowanej na pierwszej lokalizacji z poziomem powiększenia 17 przy użyciu kafelków Stamen Terrain z odpowiednią atrybucją
mapa = folium.Map(location=[data.iloc[0]['LAT'], data.iloc[0]['LON']], zoom_start=17, )

# Dodanie wskaźników na mapę z danych
for index, row in data.iterrows():
    marker = folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=row['NAME'],
        icon=folium.Icon(color='orange', icon='info-sign')
    )
    marker.add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("Map7.html")
