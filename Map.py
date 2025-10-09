import folium
my_map=folium.Map(location=[20.593,78.9629],zoom_start=5)
folium.Marker(
    location=[28.6139,77.2090],
    popup='Delhi',
    icon=folium.Icon(color='red',icon='star') ).add_to(my_map)
folium.Marker(
    location=[19.0760,72.8777],
    popup='Mumbai-Financial Hub',
    icon=folium.Icon(color='green') ).add_to(my_map)
my_map
