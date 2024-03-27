import folium 
import pandas as pd
df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
data_from_file=pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
lat=data_from_file["LAT"]
lon=data_from_file["LON"]
elev=list(df["ELEV"])

def color_procuder(elevation):
 if elevation < 1000:
  return 'green'
 elif 1000 <= elevation < 3000:
  return 'orange'
 else:
  return 'red'
 
map = folium.Map(location=[38.58,-99.09],zoom_start=4,tiles="OpenStreetMap")
fg=folium.FeatureGroup(name="Wulkany")

for lt, In, el in zip(lat,lon,elev):
 fg.add_child(
  folium.CircleMarker(
   location=[lt,In],radius=6,popup=str(el)+"maters", 
   fill_color=color_procuder(el),color='gray',fill_opacity=0.7))
 #fgpopulation=folium
map.add_child(fg)


map.save("test1.html")