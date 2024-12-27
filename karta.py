import osmnx as ox
import folium

# Загружаем данные для Иваново
place_name = "Ivanovo, Russia"
graph = ox.graph_from_place(place_name, network_type='all')

# Преобразуем граф в координаты для Folium
nodes, edges = ox.graph_to_gdfs(graph)

# Получаем центральные координаты карты
center_lat = nodes['y'].mean()
center_lon = nodes['x'].mean()

# Создаём карту с помощью folium
m = folium.Map(location=[center_lat, center_lon], zoom_start=14)

# Добавляем дороги на карту
for _, row in edges.iterrows():
    # Извлекаем координаты рёбер
    coords = list(row['geometry'].coords)
    # Преобразуем координаты в формат (lat, lon)
    lat_lon_coords = [(lat, lon) for lon, lat in coords]

    # Добавляем линию на карту
    folium.PolyLine(lat_lon_coords, color='blue', weight=1.5).add_to(m)

# Сохраняем карту в HTML файл
m.save('ivanovo_map.html')

print("Map saved as ivanovo_map.html")
