import folium
import pandas as pd

# Wczytanie danych z pliku volcanoes.txt
data = pd.read_csv('volcanoes.txt')

# Tworzenie mapy wycentrowanej na pierwszej lokalizacji z poziomem powiększenia 5 przy użyciu kafelków Stamen Terrain z odpowiednią atrybucją
mapa = folium.Map(location=[data.iloc[0]['LAT'], data.iloc[0]['LON']],zoom_start=5)

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
    marker = folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=popup,
        icon=folium.Icon(color='orange', icon='info-sign')
    )
    marker.add_to(mapa)
    
# Zapisanie mapy do pliku HTML
mapa.save("Map10.html")
