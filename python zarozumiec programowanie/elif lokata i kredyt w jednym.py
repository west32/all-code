wybor = input("jesli chcesz obliczyc wartosc lokaty wpisz 'lokata', jeśli chcesz sprawdzic "
              "swoją zdolność kredytową wpisz 'kredyt': ")
if wybor == 'kredyt':

    kwota_kredytu = float(input("na jaką kwotę chcwsz wziąć kredyt?"))
    oprocentowanie = float(input("na jakie oprocentowanie?"))
    wklad= float(input("jaki wkład własny?"))
    czas = int(input("na jaki czas w latach?"))
    przychod = float(input("jaki jest twoj przychód miesięczny?"))
    wydatki = float(input("jakie są Twoje wydatki miesięczne?"))

    rata = (kwota_kredytu * oprocentowanie /100) /12 + kwota_kredytu / (czas * 12)
    dostepne = przychod - wydatki
    wartosc =  wklad + kwota_kredytu
    wolne_hajsy= dostepne - rata
    if (0.2 * kwota_kredytu)> wklad >= (0.1 * kwota_kredytu)  and wolne_hajsy >= 2000 or wklad >= (0.2 * kwota_kredytu) and wolne_hajsy >= 1000:
        print('mozesz wzia')
    else:
        print('nie mozesz ')
elif wybor == 'lokata':
    wplata = float(input("jaką kwotę wpłaciłes? "))
    procent = float(input("jakie jest oprcoentowanie"))
    czas= int(input("na jaki okres czasu w latach?"))
    wynik = wplata * (1 + procent / 100) **czas

    print(f"na Twojej lokacie po {czas} latach bedzie {wynik:.2f} złotych ")
else:
    print(f" słowo {wybor} nie jest obsługiwane w programie na tym etapie")