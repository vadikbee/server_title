import folium

m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Лондон

# Добавление OpenStreetMap слоя
folium.TileLayer(
    'OpenStreetMap',
    attr='Map data & imagery © OpenStreetMap contributors'
).add_to(m)

m.save("map.html")
