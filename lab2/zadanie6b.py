import folium
import pandas as pd
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5)
for index, row in df.iterrows():
    popup_text = f"<b>{row['NAME']}</b><br>Height: {row['ELEV']} meters<br><a href='{row['WIKI_LINK']}' target='_blank'>More info</a>"  # Tekst do okienka pop-up z dodatkowym kodem HTML
    folium.Marker([row['LAT'], row['LON']], popup=folium.Popup(popup_text, parse_html=True)).add_to(map)
map.save("Map6b.html")
