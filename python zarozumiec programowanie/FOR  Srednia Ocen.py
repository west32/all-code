# Napisz funkcję, która podaną liczbę zamieni na zakres.
#
# Domyślnie przyjmujemy zakres jako +/- 10% podanej wartości.

# def zamien_na_zakres(liczba):
#
#     dol = liczba-.1*liczba
#     gora = 0.1*liczba + liczba
#     print(f"zakres liczby {liczba} to {dol:.1f}-{gora:.1f}")
#
# zamien_na_zakres(20)
# zamien_na_zakres(423.23)
# zamien_na_zakres(754.543)

# lub

def oblicz_zakres(liczba,prc_zakr=0.1):
    dolny_prog= prc_zakr*liczba-liczba
    gorny_prog= liczba + prc_zakr*liczba
    zakres= dolny_prog, gorny_prog
    return zakres

print(oblicz_zakres(100))
print(oblicz_zakres(199))
print(oblicz_zakres(100,prc_zakr=0.2))