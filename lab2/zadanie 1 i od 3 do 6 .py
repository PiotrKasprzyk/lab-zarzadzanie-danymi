import folium 
import pandas as pd
map = folium.Map(location=[50.04904416612195, 21.981755242425898],zoom_start=17)
folium.TileLayer('stamenterrain', attr='Stamen Terrain').add_to(map)
folium.Marker([50.04904416612195, 21.981755242425898], popup='WSIIZ Rzeszów').add_to(map)
folium.Marker([55.69296400027125, 12.599275399999998], popup='Pomnik Mała syrenka w Kopenhaga').add_to(map)
folium.Marker([49.94956953274273, 22.05961809697593], popup='WSIIZ Kielnarowa').add_to(map)
folium.Marker([50.01786019831364, 22.01524968163682], popup='Przystanek Powstańców warszawy 12 Rzeszów').add_to(map)
folium.Marker([50.01757052400629, 22.00293682581599], popup='Tu mieszkam').add_to(map)

df = pd.read_csv('C:/Users/preda/Desktop/zarzadzanie danymi/lab2/Volcanoes.txt')
#funkcja kolorów wskaznikow
#def color_by_elevation(elevation):
 #   if elevation < 1000:
  #      return 'green'
   # elif elevation < 2000:
    #    return 'orange'
    #else:
     #   return 'red'
    #funkcja markery
def icon_by_elevation(elevation):
     if elevation < 1000:
        return folium.Icon(color='green')
     elif elevation < 2000:
        return folium.Icon(color='orange')
     else:
        return folium.Icon(color='red')
# Dodaj wskaźniki na mapie dla każdego wulkanu
for index, row in df.iterrows():
    # Tworzymy popup łącząc nazwę wulkanu z jego wysokością
    #popup_html = f"<b>{row['NAME']}</b><br>Height: {row['ELEV']} meters"
    #popup = folium.Popup(popup_html, max_width=300)
    #popup_text = f"{row['NAME']} - Height: {row['ELEV']} meters"
    #folium.Marker([row['LAT'], row['LON']], popup=popup_text).add_to(map)
    #folium.Marker([row['LAT'], row['LON']], popup=popup_html).add_to(map)
    color = icon_by_elevation(row['ELEV'])
    icon = icon_by_elevation(row['ELEV'])
    folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=f"{row['NAME']} - Height: {row['ELEV']} meters",
        icon=icon
    ).add_to(map)
    #folium.CircleMarker(
     #   location=[row['LAT'], row['LON']],
      #  radius=5,
       # color=color,
        #fill=True,
        #fill_color=color,
        #fill_opacity=0.7,
        #popup=f"{row['NAME']} - Height: {row['ELEV']} meters"
   # ).add_to(map)
    wiki_link = f"https://en.wikipedia.org/wiki/{row['NAME']}"
    popup_html = f"<b><a href='{wiki_link}' target='_blank'>{row['NAME']}</a></b><br>Height: {row['ELEV']} meters"
    popup = folium.Popup(popup_html, max_width=300)
    #folium.Marker([row['LAT'], row['LON']], popup=popup).add_to(map)

map.save("Map1.html")