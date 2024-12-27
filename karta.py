import osmnx as ox
import folium
#import osmium  # Для работы с PBF файлами (закомментированная функция)

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

# Функция для добавления дорог
def add_roads(edges, map_obj):
    for _, row in edges.iterrows():
        coords = list(row['geometry'].coords)
        lat_lon_coords = [(lat, lon) for lon, lat in coords]
        folium.PolyLine(lat_lon_coords, color='blue', weight=1.5).add_to(map_obj)

# Функция для добавления зданий
def add_buildings(place_name, map_obj):
    # Загружаем здания для указанного места с помощью features_from_place
    buildings = ox.features_from_place(place_name, tags={'building': True})
    for _, row in buildings.iterrows():
        if row['geometry'].geom_type == 'Polygon':
            folium.Polygon(
                locations=[(lat, lon) for lon, lat in row['geometry'].exterior.coords],
                color='green', fill=True, fill_color='green', fill_opacity=0.5
            ).add_to(map_obj)

# Функция для добавления водоемов
def add_water_bodies(place_name, map_obj):
    # Загружаем водоемы для указанного места
    water_bodies = ox.features_from_place(place_name, tags={'natural': 'water'})
    for _, row in water_bodies.iterrows():
        if row['geometry'].geom_type == 'Polygon':
            folium.Polygon(
                locations=[(lat, lon) for lon, lat in row['geometry'].exterior.coords],
                color='blue',         # Контур водоема синего цвета
                fill=True,            # Включаем заливку
                fill_color='#CD5C5C',  #  цвет заливки #CD5C5C
                fill_opacity=0.5      # Прозрачность заливки
            ).add_to(map_obj)

# Функция для добавления подложки (например, Stamen Terrain)
def add_base_layer(map_obj):
    folium.TileLayer(
        'Stamen Terrain',
        attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL'
    ).add_to(map_obj)

# Закомментированная функция для добавления данных из PBF файла
# def add_data_from_pbf(pbf_file, map_obj):
#     # Пример обработки PBF файла с использованием osmium
#     # Создаем объект osmium для чтения PBF
#     class Handler(osmium.SimpleHandler):
#         def __init__(self):
#             super().__init__()
#             self.buildings = []
#             self.roads = []
#
#         def area(self, a):
#             # Сохраняем полигоны зданий
#             if 'building' in a.tags:
#                 self.buildings.append(a)
#
#         def way(self, w):
#             # Сохраняем дороги (если это way с тегом highway)
#             if 'highway' in w.tags:
#                 self.roads.append(w)
#
#     # Создаем обработчик для чтения данных из PBF
#     handler = Handler()
#     handler.apply_file(pbf_file)
#
#     # Добавляем найденные здания и дороги на карту
#     for building in handler.buildings:
#         if building.is_closed():
#             coords = [(lat, lon) for lon, lat in building.nodes]
#             folium.Polygon(locations=coords, color='green', fill=True, fill_color='green', fill_opacity=0.5).add_to(map_obj)
#
#     for road in handler.roads:
#         coords = [(lat, lon) for lon, lat in road.nodes]
#         folium.PolyLine(coords, color='blue', weight=1.5).add_to(map_obj)

# Добавляем элементы на карту
add_base_layer(m)  # Добавляем подложку
add_roads(edges, m)  # Добавляем дороги
add_buildings(place_name, m)  # Добавляем здания
add_water_bodies(place_name, m)  # Добавляем водоемы

# Пример использования закомментированной функции:
# add_data_from_pbf('123', m)  # Замените на путь к вашему .pbf файлу

# Сохраняем карту в HTML файл
m.save('ivanovo_map_full.html')

print("Map saved as ivanovo_map_full.html")
