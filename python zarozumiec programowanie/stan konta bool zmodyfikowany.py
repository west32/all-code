# Zmodyfikuj program obliczający wartość lokaty, tak aby dodatkowo wypisywał informacje,
# czy w planowanym okresie łączna wartość inwestycji wzrośnie o co najmniej 10%.

wplata = float(input("jaką kwotę wpłaciłes? "))
procent = float(input("jakie jest oprcoentowanie"))
czas= int(input("na jaki okres czasu w latach?"))
wynik = wplata * (1 + procent / 100) **czas

print(f"na Twojej lokacie po {czas} latach bedzie {wynik:.2f} złotych ")

przyrost = (wynik-wplata) / wplata * 100

print(f"łączna wartość inwestycji wynosi wiecej niż 10%? \t\t\t {przyrost >= 10}")