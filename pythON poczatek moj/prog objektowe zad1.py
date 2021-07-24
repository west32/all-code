# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
#
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
#
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy
# produktów, a wartościami instancje klasy produkt.

class Product:
    pass
class  Order:
    pass
class Apple:
    pass
class Potato:
    pass
if __name__=='__main__':
    jabłko1 = Apple()
    jabłko2= Apple()
    ziemniak1 = Potato()
    ziemniak2 = Potato()
    print(type(jabłko1))
    print(type(jabłko2))
    print(type(ziemniak1))
    print(type(ziemniak2))

    Orders= [Order(),Order(),Order(),Order(),Order()]

    Products = {
        "mleko": Product(),
        "banany": Product(),
        "białko": Product()
    }

    print(Orders)
    print(Products)