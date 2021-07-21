# Napisz funkcję liczącą prędkość średnią na podstawie zadanego dystansu i czasu.
#
# Następnie wykorzystaj ją implementując program, który wyznaczy:
#
# średnią prędkość biegu
# średnią prędkość jazdy na rowerze
# średnią prędkość jazdy autem

# def calculate_avg_speed(disatnce,time):
#     return disatnce/time
#
# def avg_speed_for(vehicle_type):
#     distance= float(input(f"jaki dystans przebyłeś w trakcie {vehicle_type}?"))
#     time= float(input("w jakim czasie(w godzinach)? "))
#     average_speed= calculate_avg_speed(distance,time)
#     print (f" Twoja srednia prędkość w trakcie przemiszczania sie za pomocą {vehicle_type} wynosila {average_speed:.0f}km/h")
#
# avg_speed_for("roweru")

def calculate_avg_speed(disatnce,time):
    return disatnce/time

def avg_speed_for(distance,time,vehicle_type):

    average_speed= calculate_avg_speed(distance,time)
    print (f" Twoja srednia prędkość w trakcie przemiszczania sie za pomocą {vehicle_type} wynosila {average_speed:.0f}km/h")

avg_speed_for(distance=20,time=1,vehicle_type="roweru")