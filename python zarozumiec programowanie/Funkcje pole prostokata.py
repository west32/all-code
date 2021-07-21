def zapytaj_o_int_wartosc(wiadomosc):
    wartosc_input = input(wiadomosc)
    return int (wartosc_input)

a= 0
b= 0
def oblicz_pole_prostokata (a,b):
    a = zapytaj_o_int_wartosc("podaj długość boku a")
    b = zapytaj_o_int_wartosc("podaj dlugosc boku b")
    pole = a*b
    return a * b




print(f"pole prostokąta o podanych wymiarach wynosi {oblicz_pole_prostokata(a,b)} cm ")


