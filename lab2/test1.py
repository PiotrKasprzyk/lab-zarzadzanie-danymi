import folium

# Create a Map instance
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13, control_scale=True, prefer_canvas=True)

# Add Stamen Terrain layer
folium.TileLayer('Stamen Terrain', attr='Map data © OpenStreetMap contributors').add_to(m)

# Save it as html
m.save('XD.html')