# Napisz kalkulator dla kredytu o malejącej racie. Zapytaj użytkownika o:
# -> Kwotę kredytu
# -> Oprocentowanie kredytu
# -> Czas trwania (w latach)
# -> Koszty początkowe (prowizja itp.)
# Oblicz jaką łącznie sumę użytkownik odda bankowi i porównaj ją z kapitałem, który otrzyma.
# PodpowiedĹş: oblicz wartość każdej miesięcznej raty według wzoru:
# kapitał spłacany miesięcznie = kwota kredytu / (liczba lat * 12)
# pozostały kapitał = kwota kredytu - (numer miesiąca od początku - 1) * kapitał spłacany miesięcznie
# rata = (pozostały kapitał * oprocentowanie / 100) / 12 + kapitał spłacany miesięcznie

kwota_kredytu = int(input("na jaką kwote kredyt?"))
oprocentowanie = float(input('na jaki procent?'))
czas = int(input('na jaki czas?'))
koszty_poczatek = float(input('jakie koszty poczatkowe'))
kapital_splacany_miesiecznie = kwota_kredytu / (czas * 12)
liczba_rat= int(czas * 12)
oddana_kwota = koszty_poczatek
for miesiac in range (1,liczba_rat +1):
    pozostaly_kapital = kwota_kredytu - (miesiac -1) * kapital_splacany_miesiecznie
    rata = (pozostaly_kapital * oprocentowanie / 100) /12 + kapital_splacany_miesiecznie
    print(f"rata za {miesiac} miesiąc wynosi {rata:.0f} ")
    oddana_kwota += rata

print (f"roznica miedzy kapitalem którym otrzyałes: {kwota_kredytu} a sumą którą oddałeś bankowi {oddana_kwota:.0f} złotych")
