# Wczytaj od użytkownika informacje o:
#
# Początkowym kapitale (wpłaconej kwocie)
# Oprocentowaniu
# Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations,
# a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.
#
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat
print(__name__)
def calculate_value(initial,perc,time):
    result= initial * (1+perc/100)** time
    return result
