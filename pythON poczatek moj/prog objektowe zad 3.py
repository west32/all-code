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
#
# Podziel projekt - utwórz nowy pakiet shop i przenieś do osobnych modułów (plików) w pakiecie store:
# Klasę Apple
# Klasę Potato
# Klasę Product oraz funkcje generujące i wypisujące produkt
# Klasę Order oraz funkcje generujące i wypisujące zamówienie
# Utwórz skrypt uruchomieniowy main, który importuje i wykorzystuje powyższe klasy i funkcje
import random


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
def print_product (product):
    print(f"Product: {product.name}    |Kategoria: {product.category}     |cena: {product.prize}")
def print_order (order):
    print(20*"=")
    print(f"zamówienie dla : {order.orderer_first_name} {order.orderer_last_name}")
    print("zamówione produkty:")
    for product in order.products_list:
        print("\t", end="")
        print_product(product)
    print(f"łączna kwota do zapłaty to: {order.total_prize} PLN")
    print(20 * "=")
    print()
def generate_an_order():
    number_of_products= random.randint(1,20)
    products= []
    for product_number in range (number_of_products):
        product_name= f"Product- {product_number}"
        product_category = "inne"
        product_prize = random.randint(1,30)
        product = Product (product_name,product_category,product_prize)
        products.append(product)
    order = Order("Bartłomiej", "Juda",products)
    return order

def run_homework ():
    green_Apple = Apple ("green", "small", 4.5)
    red_apple = Apple ("red", "big", 6.5)


    old_potato = Potato("old", "medium", 2)


    cookie = Product ("cookie","food",3)
    milk = Product ("milk","food", 5)
    Bartek_order = Order ("Bartek","Juda",products_list=[cookie,milk])
    first_order= generate_an_order()
    print_order(first_order)
    second_order = generate_an_order()
    print_order(second_order)
    print_order(Bartek_order)


if __name__ == '__main__':
    run_homework()

