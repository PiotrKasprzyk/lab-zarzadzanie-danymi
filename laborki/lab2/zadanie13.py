import folium
import json

# Utworzenie mapy wycentrowanej na Polsce
mapa = folium.Map(location=[52.237049, 21.017532], zoom_start=6)

# Dodanie warstwy Polygon z pliku world.json
with open('world.json') as f:
    geojson_data = json.load(f)

folium.GeoJson(
    geojson_data,
    name='geojson'
).add_to(mapa)

# Dodanie warstwy kontroli
folium.LayerControl().add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("Map13.html")
