
import folium

# Create a map centered at the specified location with a zoom level of 17 using Stamen Terrain tiles with proper attribution
map = folium.Map(location=[50.04904416612195, 21.981755242425898], 
                 zoom_start=17, 
                 tiles='CartoDB Positron', 
                 attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.')

# Save the map to an HTML file
map.save("Map2v1.html")