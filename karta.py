import folium

# Создание карты с начальной позицией
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Лондон

# Добавление слоя с тайлами Stamen Terrain
# Закомментировано, чтобы избежать конфликта с другими слоями
# folium.TileLayer(
#     'Stamen Terrain',
#     attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
# ).add_to(m)

# Добавление слоя с тайлами OpenStreetMap
folium.TileLayer(
    'OpenStreetMap',
    attr='Map data & imagery © OpenStreetMap contributors'
).add_to(m)

# Добавление слоя с тайлами CartoDB Positron
# Закомментировано, чтобы избежать конфликта с другими слоями
# folium.TileLayer(
#     'cartodb positron',
#     attr='&copy; <a href="https://carto.com/attributions">CartoDB</a>'
# ).add_to(m)

# Добавление слоя с тайлами Stamen Toner
# Закомментировано, чтобы избежать конфликта с другими слоями
# folium.TileLayer(
#     'Stamen Toner',
#     attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
# ).add_to(m)

# Сохранение карты в HTML файл
m.save("map.html")
