# Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i
# pokonanego dystansu (prędkość = dystans / czas) i umieść ją w jednym pliku.
#
# W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika i wywołaj funkcję - oblicz prędkość średnią.

import modul_avg_speed

distance= float(input("jaki dystans pokonales? "))
time= float(input("w jakim czasie?",))

avg_speed = modul_avg_speed.calculate_avg(distance,time)

print(f"Twoja srednia prędkość wynosila {avg_speed:.0f} km/h")