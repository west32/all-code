# def pole_prostokąta(a,b):
#     pole= a * b
#     return pole
#
# def run_example():
#     bok_a = int(input("podaj pole boku a "))
#     bok_b = int(input("podaj pole boku b "))
#
#     print(pole_prostokąta(bok_a,bok_b))
#
# if __name__=="__main__":
#     run_example()

# 2

# Napisz funkcję liczącą prędkość średnią na podstawie zadanego dystansu i czasu.
#
# Następnie wykorzystaj ją implementując program, który wyznaczy:
#
# średnią prędkość biegu
# średnią prędkość jazdy na rowerze
# średnią prędkość jazdy autem

def avg_speed(distance,time):
    return distance/time

def run_homework():
    run_distance= float(input("jaki dystans przebiegłęs (w km)? "))
    run_time= float(input("ile Ci to zajeło (w h)? "))
    print(f"Twoja średnia prędkość biegu wynosiłą {avg_speed(run_distance,run_time):.2f} km/h")

if __name__=="__main__":
    run_homework()