import folium 
import pandas as pd
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
data_from_file=pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')

#print(data_from_file)
#print(f'Type of data{type(df)}')
#print(f'Type of some (selected) column:{type(data_from_file["NAME"])}')
lat=data_from_file["LAT"]
lon=data_from_file["LON"]
elev=list(df["ELEV"])


#print(f'LAT={lat}')
#print(f'TYPE(LON)={type(lat)}')

#print(f'LAT={lat}')
#print(f'TYPE(LON)={type(lat)}')


map = folium.Map(location=[38.58,-99.09],zoom_start=4,tiles="OpenStreetMap")
fg=folium.FeatureGroup(name="Moja Mapa")

for lt, In, el in zip(lat,lon,elev):
 fg.add_child(folium.Marker(location=[lt,In],popup=str(el), icon=folium.Icon(color='orange')))
map.add_child(fg)


map.save("test.html")