import folium
import pandas as pd
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5)
for index, row in df.iterrows():
    popup_text = f"{row['NAME']} - Height: {row['ELEV']} meters"  # Tekst do okienka pop-up
    folium.Marker([row['LAT'], row['LON']], popup=popup_text).add_to(map)
map.save("Map5.html")
