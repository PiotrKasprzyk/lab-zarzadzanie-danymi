import folium
import json

# Funkcja do określania koloru w zależności od populacji
def get_color(population):
    if population < 1000000:
        return '#ffffcc'  # Light yellow
    elif 1000000 <= population < 10000000:
        return '#ffeda0'  # Light orange
    elif 10000000 <= population < 50000000:
        return '#feb24c'  # Orange
    elif 50000000 <= population < 100000000:
        return '#fd8d3c'  # Dark orange
    else:
        return '#e31a1c'  # Red

# Funkcja do stylizowania warstwy Polygon
def style_function(feature):
    population = feature['properties'].get('POP2005', 0)  # Zakładając, że liczba ludności jest w polu 'POP2005'
    return {
        'fillColor': get_color(population),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
    }

# Utworzenie mapy wycentrowanej na Polsce
mapa = folium.Map(location=[52.237049, 21.017532], zoom_start=4)

# Dodanie warstwy Polygon z pliku world.json
with open('world.json') as f:
    geojson_data = json.load(f)

folium.GeoJson(
    geojson_data,
    name='geojson',
    style_function=style_function
).add_to(mapa)

# Dodanie warstwy kontroli
folium.LayerControl().add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("Map15.html")
