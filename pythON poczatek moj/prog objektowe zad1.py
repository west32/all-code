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
import random

class Product:
    def __init__(self,name,category_name,prize):
        self.name = name
        self.category_name = category_name
        self.prize = prize
class  Order:
    def __init__(self,orderer_first_name,orderer_last_name,products_list=None):
        self.orderer_last_name = orderer_last_name
        if products_list is None:
            products_list = []
        self.product_list = products_list
        self.orderer_first_name = orderer_first_name
        total_prize = 0
        for product in products_list:
            total_prize += product.prize
        self.total_prize= total_prize


class Apple:
    def __init__(self,species_name,size,prize_for_kg):
        self.species_name = species_name
        self.size = size
        self.prize_for_kg = prize_for_kg
class Potato:
    def __init__(self, species_name, size, prize_for_kg):
        self.species_name = species_name
        self.size = size
        self.prize_for_kg = prize_for_kg

eggs= Product(name= 'z_wolnego_wybiegu',category_name='nabiał',prize=1)
milk = Product(name='łaciate',category_name='nabiał',prize=2)
orange= Product(name="nice",category_name="fruits",prize=3)

piotr_order= Order("Piotr","Sochacki", products_list=[eggs,milk,orange])

green_apple = Apple("green","big",3)
red_apple = Apple('red','small',2)
dark_red_appl = Apple ('dark red', 'xxl',5)

old_potato = Potato('old','big', 1)
young_potato = ('young','small',1.5)

def print_product (product):
    print(f"produkt : {product.name}, category: {product.category_name}, prize: {product.prize}")
def print_order(order):
    print(f"Zamowienie Dla {order.orderer_first_name}{order.orderer_last_name} lista produktów:")
    for product in order.product_list:

        print_product(product)
    print(f"Łączna kwota zamówienia to: {order.total_prize}")

def order_with_random_products_list(order_first_name,order_last_name):
    number_of_products = random.randint(1,20)
    products_list=[]
    for product_number in range (number_of_products):
        product_name= f"Product-{product_number}"

    order=Order(order_first_name,order_last_name,)
    return order




if __name__=='__main__':
    order= piotr_order
    print_order(order)

