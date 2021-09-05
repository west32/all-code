import random
import folium
SANDOMIERZ_CENTER_POSITION = [50.68265685,21.74839680]
MAP_FILE_LOCATION = "mapers.html"

def random_point():
    return random.uniform(50.1,51.0), random.uniform(21.1,22.0)

def generate_example_map():
    generated_map = folium.Map(location=SANDOMIERZ_CENTER_POSITION, zoom_start=13)

    for number in range(20):
        generated_map.add_child(
            folium.CircleMarker(
                location=random_point(),
                fill= "true",
                radius=8,
                popup = str(number),
                fill_collor= "clear",
                fill_opacity=1,
            )
        )

    folium.PolyLine([random_point(), random_point()],color="red", weight=3.5, opacity=1).add_to(generated_map)

    generated_map.save(MAP_FILE_LOCATION)
    print(generated_map)

def run_example():
    generate_example_map()