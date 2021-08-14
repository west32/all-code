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

from shop.class_product import Product
from shop.class_Order_element import OrderElement

MIN_QUANTITY = 1
MIN_PRICE = 1
MIN_ORDER_ELEMENTS = 1
MAX_ORDER_ELEMENTS = 5
MAX_PRIZE = 50
MAX_QUANTITY = 6


def generate_order_elements(number_of_products = None):
    if number_of_products is None:
        number_of_products = random.randint(MIN_ORDER_ELEMENTS, MAX_ORDER_ELEMENTS)

    order_elements = []
    for product_number in range(number_of_products):
        product_name = f"Produkt-{product_number}"
        category_name = "Inne"
        unit_price = random.randint(MIN_PRICE, MAX_PRIZE)
        product = Product(product_name, category_name, unit_price)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        order_elements.append(OrderElement(product, quantity))

    return order_elements
