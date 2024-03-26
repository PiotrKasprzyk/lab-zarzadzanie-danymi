import folium
import pandas as pd
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5)
for index, row in df.iterrows():
    folium.Marker([row['LAT'], row['LON']], popup=row['NAME']).add_to(map)
map.save("Map4.html")
