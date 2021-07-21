# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
#
# Wczytaj od użytkownika informacje o:
#
# Początkowym kapitale (wpłaconej kwocie)
# Oprocentowaniu
# Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations,
# a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.
#
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

import calculations.funkcja_calculate
initial= float(input("jaki kapital? "))
perc= int(input("jakie oprcentowanie? "))
time= int(input("ile lat? "))
import calculations.funkcja_calculate




value= calculations.funkcja_calculate.calculate_value(initial,perc,time)
print(f" po {time} latach Twoja lokata bedzie warta: {value:.1f} złotych ")