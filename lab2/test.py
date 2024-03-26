import folium
import pandas as pd

# Utworzenie obiektu mapy (domyślny widok OpenStreetMap)
map_osm = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Utworzenie obiektu mapy (widok Stamen Terrain)
map_terrain = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Utworzenie obiektu mapy (widok CartoDB Positron)
map_positron = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Utworzenie obiektu mapy (widok Stamen Terrain) z wskaźnikiem
map_with_marker = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
folium.Marker([51.5074, -0.1278], popup='London').add_to(map_with_marker)

# Utworzenie obiektu mapy z kilkoma wskaźnikami
map_with_markers = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
folium.Marker([51.5074, -0.1278], popup='London').add_to(map_with_markers)
folium.Marker([48.8566, 2.3522], popup='Paris').add_to(map_with_markers)
folium.Marker([40.7128, -74.0060], popup='New York City').add_to(map_with_markers)

# Wczytanie danych z pliku *.csv (przykładowy plik z danymi wulkanów)
df =pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')

# Interaktywna mapa z markami z pliku *.csv
map_with_markers_from_csv = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=3)
for index, row in df.iterrows():
    folium.Marker([row['LAT'], row['LON']], popup=row['NAME']).add_to(map_with_markers_from_csv)

# Okno pop-up z dodatkowym kodem HTML
html_popup = """
<h1>London</h1>
<p>Capital city of England.</p>
"""
popup_with_html = folium.Popup(html_popup, max_width=300)

map_with_popup = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
folium.Marker([51.5074, -0.1278], popup=popup_with_html).add_to(map_with_popup)

# Kolorowanie punktów/markerów zależnie od wysokości obiektu (wulkanu)
map_with_colored_markers = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=3)
for index, row in df.iterrows():
    if row['ELEV'] < 1000:
        color = 'green'
    elif row['ELEV'] < 2000:
        color = 'orange'
    else:
        color = 'red'
    folium.CircleMarker([row['LAT'], row['LON']], radius=5, color=color, fill=True, fill_color=color).add_to(map_with_colored_markers)

# Interaktywna mapa internetowa z kolejną 3-cią warstwą – typu Polygon layer
world_geojson = 'C:/Users/preda/Desktop/zarzadzanie danymi/lab2/world.json'
world_map_with_polygons = folium.Map(location=[0, 0], zoom_start=2)
folium.GeoJson(world_geojson).add_to(world_map_with_polygons)

# Interaktywna mapa internetowa z różnymi kolorami dla państw, w zależności od liczby ludności
df_population = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Populations.txt')
population_dict = df_population.set_index('Country')['Population'].to_dict()

world_map_population = folium.Map(location=[0, 0], zoom_start=2)
folium.GeoJson(
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
).add_to(world_map_population)

# Interaktywna mapa internetowa (finalny wygląd GUI – z oknem pop-up do włączania/wyłączania warstw dodatkowych – Markers oraz/lub Polygons)
final_map = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
folium.Marker([51.5074, -0.1278], popup='London').add_to(final_map)
folium.LayerControl().add_to(final_map)




# Zapisz mapę do pliku HTML
final_map.save("testcodemap.html")
