import folium
import pandas as pd

# Utwórz mapę i ustaw jej początkowe współrzędne oraz zoom
map = folium.Map(location=[0, 0], zoom_start=2)

# Dodaj warstwę Stamen Terrain
folium.TileLayer('stamenterrain', attr='Stamen Terrain').add_to(map)

# Wczytaj dane z pliku tekstowego dotyczącego wulkanów
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')

# Wczytaj dane z pliku GeoJSON dotyczącego obszarów krajów
world_geojson = 'C:/Users/preda/Desktop/zarzadzanie danymi/lab2/world.json'

for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['LAT'], row['LON']],
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.7,
        popup=f"{row['NAME']} - Height: {row['ELEV']} meters"
    ).add_to(map)

# Dodaj warstwę polygonalną dla obszarów krajów
folium.GeoJson(
    world_geojson,
    name='Countries',
    style_function=lambda x: {'fillColor': 'blue', 'fillOpacity': 0.3, 'color': 'blue'}
).add_to(map)

# Dodaj kontrolę warstw
folium.LayerControl().add_to(map)

# Zapisz mapę do pliku HTML
map.save("InteractiveMap.html")