import folium
import pandas as pd

# Utwórz mapę i ustaw jej początkowe współrzędne oraz zoom
map = folium.Map(location=[50.04904416612195, 21.981755242425898], zoom_start=5)

# Dodaj warstwę Stamen Terrain
folium.TileLayer('stamenterrain', attr='Stamen Terrain').add_to(map)

# Wczytaj dane z pliku tekstowego
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')

# Określ ikonę w zależności od wysokości wulkanu
def icon_by_elevation(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 2000:
        return 'orange'
    else:
        return 'red'

# Dodaj markery na mapie dla każdego wulkanu
for index, row in df.iterrows():
    color = icon_by_elevation(row['ELEV'])
    folium.CircleMarker(
        location=[row['LAT'], row['LON']],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=f"{row['NAME']} - Height: {row['ELEV']} meters"
    ).add_to(map)

# Zapisz mapę do pliku HTML
map.save("Map8.html")