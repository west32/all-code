# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
#
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
#
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy
# produktów, a wartościami instancje klasy produkt.

class Produkt:
    pass
class Zamówienie:
    pass
class Jabłko:
    pass
class Ziemiak:
    pass
if __name__=='__main__':
    jabłko1 = Jabłko()
    jabłko2= Jabłko()
    ziemniak1 = Ziemiak()
    ziemniak2 = Ziemiak()
    print(type(jabłko1))
    print(type(jabłko2))
    print(type(ziemniak1))
    print(type(ziemniak2))

    Orders= [Zamówienie(),Zamówienie(),Zamówienie(),Zamówienie(),Zamówienie()]