import folium
import pandas as pd

# Wczytanie danych z pliku volcanoes.txt
data = pd.read_csv('volcanoes.txt')

# Funkcja do określania koloru markera w zależności od wysokości wulkanu
def get_marker_color(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

# Tworzenie mapy wycentrowanej na pierwszej lokalizacji z poziomem powiększenia 5 przy użyciu kafelków Stamen Terrain z odpowiednią atrybucją
mapa = folium.Map(location=[data.iloc[0]['LAT'], data.iloc[0]['LON']], zoom_start=5)

# Dodanie wskaźników na mapę z danych
for index, row in data.iterrows():
    wiki_url = f"https://en.wikipedia.org/wiki/{row['NAME'].replace(' ', '_')}"
    popup_content = f"""
    <div style="font-family: Arial, sans-serif; font-size: 14px;">
        <h4 style="margin-bottom: 10px;">Nazwa wulkanu: <a href="{wiki_url}" target="_blank">{row['NAME']}</a></h4>
        <p>Wysokość: {row['ELEV']} m</p>
    </div>
    """
    popup = folium.Popup(popup_content, max_width=300)
    marker_color = get_marker_color(row['ELEV'])
    circle_marker = folium.CircleMarker(
        location=[row['LAT'], row['LON']],
        radius=8,
        popup=popup,
        color='black',
        fill=True,
        fill_color=marker_color,
        fill_opacity=0.7
    )
    circle_marker.add_to(mapa)

# Zapisanie mapy do pliku HTML
mapa.save("Map12.html")
