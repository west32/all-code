import random
import folium

SND_CENTER_POSITION= [50.68265685,21.74839680]
MAP_FILE_LOCATION = "nap.html"

def random_points():
    return  random.uniform(50.5,50.7), random.uniform(21.6,21.8)

def generate_example_map():
    generated_map = folium.Map(location=SND_CENTER_POSITION,zoom_start=14)

    for number in range (10):
        generated_map.add_child(folium.CircleMarker(
            location= random_points(),
            fill="true",
            radius= 5,
            popup=str(number),
            fill_color="red",
            color="clear",
            fill_opacity=1,
        ))

    generated_map.save(MAP_FILE_LOCATION)

def run_example():
    generate_example_map()

if __name__ =="__main__":
    run_example()