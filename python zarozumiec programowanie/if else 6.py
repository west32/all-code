# Napisz uproszczony kalkulator kredytowy.
#
# Celem kalkulatora jest sprawdzenie czy użytkownika stać na kredyt hipoteczny o podanych parametrach.
#
# Zapytaj użytkownika o:
#
# kwotę kredytu
# oprocentowanie kredytu
# wartość wkładu własnego
# czas kredytowania w latach
# przychód miesięczny
# sumę miesięcznych wydatków
#
# Oblicz ratę ze wzoru:
# (kwota kredytu * oprocentowanie / 100) / 12 + kwota kredytu / (liczba lat * 12)
#
#
# Oblicz dostępne środki jako:
# przychód - suma wydatków
#
#
# Oblicz wartość nieruchomości jako:
# wkład własny + kwota kredytu

kwota_kredytu = float(input("na jaką kwotę chcwsz wziąć kredyt?"))
oprocentowanie = float(input("na jakie oprocentowanie?"))
wklad= float(input("jaki wkład własny?"))
czas = int(input("na jaki czas w latach?"))
przychod = float(input("jaki jest twoj przychód miesięczny?"))
wydatki = float(input("jakie są Twoje wydatki miesięczne?"))

rata = (kwota_kredytu * oprocentowanie /100) /12 + kwota_kredytu / (czas * 12)
dostepne = przychod - wydatki
wartosc =  wklad + kwota_kredytu

# if wklad >= 0.1 * kwota_kredytu:
#     wklad_ok = True
# else:
#     wklad_ok = False
# if not wklad_ok:
#     print ('nie mozesz otrzymac kredytu')
# if wklad_ok:
#     if wklad_ok > 0.2 * kwota_kredytu and dostepne >= (rata + 1000) or wklad_ok < 0.2 * kwota_kredytu and dostepne >= (rata +2000):
#         print('otrzymasz kredyt')
#     else:
#         print('nie otrzymasz')

# lub

wolne_hajsy= dostepne - rata

# if(0.2 * kwota_kredytu)> wklad >= (0.1 * kwota_kredytu)  and wolne_hajsy >= 2000 or wklad >= (0.2 * kwota_kredytu) and wolne_hajsy >= 1000:
#     print('mozesz wzia')
#     print('mozesz')
# else:
#     print('nie mozesz ')
# lub

if(0.2 * kwota_kredytu)> wklad >= (0.1 * kwota_kredytu)  and wolne_hajsy >= 2000:
    print('mozesz wzia')

else:
    if wklad >= (0.2 * kwota_kredytu) and wolne_hajsy >= 1000:
        print('mozesz ')
    else:
        print('nie mozesz ')

