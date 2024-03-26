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
        return folium.Icon(color='green')
    elif elevation < 2000:
        return folium.Icon(color='orange')
    else:
        return folium.Icon(color='red')

# Dodaj markery na mapie dla każdego wulkanu
for index, row in df.iterrows():
    icon = icon_by_elevation(row['ELEV'])
    # Tworzymy link do strony Wikipedii
    wiki_link = f"https://en.wikipedia.org/wiki/{row['NAME']}"
    # Tworzymy popup z dodatkowym kodem HTML
    popup_html = f"<b><a href='{wiki_link}' target='_blank'>{row['NAME']}</a></b><br>Height: {row['ELEV']} meters"
    folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=popup_html,
        icon=icon
    ).add_to(map)

# Zapisz mapę do pliku HTML
map.save("Map7.html")
