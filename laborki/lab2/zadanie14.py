import folium
import json

# Funkcja do stylizowania warstwy Polygon
def style_function(feature):
    return {
        'fillColor': 'yellow',
        'color': 'blue',
        'weight': 1,
        'dashArray': '5, 5',
        'fillOpacity': 0.5,
    }

# Utworzenie mapy wycentrowanej na Polsce
mapa = folium.Map(location=[52.237049, 21.017532], zoom_start=6)

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
mapa.save("Map14.html")
