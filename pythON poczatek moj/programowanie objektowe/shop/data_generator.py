# Zrefaktoryzuj rozwiązanie zadania drugiego z lekcji funkcja
# jako obiekt z modułu Programowanie Obiektowe I.
#
# Jest to zadanie, w którym dodawaliśmy polityki rabatowe.**
#
# Utwórz nowy moduł data_generator i przenieś do niego z pliku
# main funkcję generującą elementy zamówienia.
#
# Ulepsz tę funkcję dodając do niej parametr liczby produktów w
# zamówieniu z domyślną wartością None (jeżeli nie przekazano oczekiwanej
# liczby produktów to wylosuj ją z zakresu od 1 do maksymalnej liczby pozycji w zamówieniu).
#
# Zastąp graniczne wartości, z których generowana jest liczba produktów w
# pozycji zamówienia oraz cena jednostkowa produktu stałymi, czyli zapisanymi
# według odpowiedniej konwencji zmiennymi globalnymi na poziomie nowo utworzonego
# modułu data_generator.
#
# Usuń nieużywaną metodę klasy Order: generate_order.
#

import random

from shop.class_product import Product,ProductCategory
from shop.class_Order_element import OrderElement

MIN_QUANTITY = 1
MIN_PRICE = 1
MIN_ORDER_ELEMENTS = 1
MAX_ORDER_ELEMENTS = 5
MAX_PRIZE = 50
MAX_QUANTITY = 6

def generate_quantity():
    return random.randint(MIN_QUANTITY, MAX_QUANTITY)

def generate_product(name=None):

    category=ProductCategory.FOOD
    unit_price = random.randint(MIN_PRICE,MAX_PRIZE)
    identifier = random.randint(1,300)
    if name is None:
        name= f"product = {identifier}"

    return Product(name,category,unit_price,identifier)

def generate_order_elements(products_to_generate = None):
    if products_to_generate is None:
        products_to_generate = random.randint(1,MAX_ORDER_ELEMENTS)

    order_elements = []
    for product_number in range(products_to_generate):
        product_name = f"Produkt-{product_number}"
        product = generate_product(product_name)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY,)
        order_elements.append(OrderElement(product, quantity))



    return order_elements
