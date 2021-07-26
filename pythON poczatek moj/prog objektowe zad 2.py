# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:
#
# Product: nazwa, nazwa kategorii, cena jednostkowa
# Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena
# (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
# Apple: nazwa gatunku, rozmiar, cena za kg
# Potato: nazwa gatunku, rozmiar, cena za kg
# Utwórz kilka obiektów każdej klasy.
# Napisz funkcję wypisującą produkt i zamówienie.
# Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.
# Napisz funkcję generującą zamówienie z losową listą produktów na przykład:
# Produkt-1, Produkt-2 itd.
class  Product:
    def __init__(self,name,category,prize):
        self.name = name
        self.category = category
        self.prize = prize

class Order:
    def __init__(self,orderer_first_name, orderer_last_name,products_list=None):
        if products_list is None:
            products_list = []
        self.products_list = products_list
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        total_prize = 0
        for product in products_list:
            total_prize += product.prize
        self.total_prize = total_prize

class Apple :
    def __init__(self, species_name, size, prize_per_kg):
        self.size = size
        self.species_name = species_name
        self.prize_per_kg = prize_per_kg

class Potato :
    def __init__(self, species_name, size, prize_per_kg):
        self.size = size
        self.species_name = species_name
        self.prize_per_kg = prize_per_kg

def run_homework ():
    green_Apple = Apple ("green", "small", 4.5)
    red_apple = Apple ("red", "big", 6.5)
    print(green_Apple)
    print(red_apple)

    old_potato = Potato("old", "medium", 2)
    print(old_potato)

    cookie = Product ("cookie","food",3)
    print(cookie)

    Bartek_order= Order ("Bartek","Juda",products_list=[cookie])
    print(Bartek_order)

if __name__ == '__main__':
    run_homework()
