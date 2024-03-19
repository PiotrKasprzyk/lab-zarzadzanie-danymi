import folium
import pandas as pd

# Utwórz mapę i ustaw jej początkowe współrzędne oraz zoom
map = folium.Map(location=[0, 0], zoom_start=2)

# Dodaj warstwę Stamen Terrain
folium.TileLayer('stamenterrain', attr='Stamen Terrain').add_to(map)

# Wczytaj dane z pliku GeoJSON dotyczącego obszarów krajów
world_geojson = 'C:/Users/preda/Desktop/zarzadzanie danymi/lab2/world.json'

# Wczytaj dane z pliku tekstowego dotyczącego populacji państw
df_population = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Populations.txt')

# Stwórz słownik z krajami jako kluczami i populacją jako wartościami
population_dict = df_population.set_index('Country')['Population'].to_dict()

# Dodaj warstwę polygonalną dla obszarów krajów z dynamicznymi kolorami
geojson_layer = folium.GeoJson(
    world_geojson,
    name='Countries',
    style_function=lambda feature: {
        'fillColor': 'green' if population_dict.get(feature['properties']['NAME']) is None else 
                     'red' if population_dict.get(feature['properties']['NAME']) > 100000000 else 
                     'orange' if population_dict.get(feature['properties']['NAME']) > 50000000 else 
                     'yellow' if population_dict.get(feature['properties']['NAME']) > 10000000 else 
                     'blue' if population_dict.get(feature['properties']['NAME']) > 5000000 else 
                     'purple',
        'fillOpacity': 0.6,
        'color': 'black',
        'weight': 1
    }
).add_to(map)

# Dodaj warstwę markerów dla wulkanów
volcanoes_layer = folium.FeatureGroup(name='Volcanoes').add_to(map)

# Wczytaj dane z pliku tekstowego dotyczącego wulkanów
df_volcanoes = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')

# Dodaj markery dla wulkanów
for index, row in df_volcanoes.iterrows():
    wiki_link = f"https://en.wikipedia.org/wiki/{row['NAME']}"

    folium.CircleMarker(
        location=[row['LAT'], row['LON']],
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.7,
        popup=f"{row['NAME']} - Height: {row['ELEV']} meters"
    ).add_to(volcanoes_layer)

# Dodaj kontrolę warstw
folium.LayerControl(collapsed=False).add_to(map)

# Zapisz mapę do pliku HTML
map.save("InteractiveMap_Final.html")
