# Napisz nową klasę: OrderElement, która będzie reprezentować
# pozycję w zamówieniu. Taka pozycja będzie zawierać informacje
# o produkcie i liczbie jego sztuk w zamówieniu.
# W klasie OrderElement zaimplementuj metodę wypisującą
# (info o liczbie elementów i produkcie) oraz obliczającą cenę danej pozycji w zamówieniu.
#
# W klasie Order zastąp listę produktów listą pozycji w zamówieniu
# (zmodyfikuj niezbędne funkcje, np. generowanie zamówienia).
# Napisz metodę obliczającą łączną wartość zamówienia jako sumę wartości wszystkich pozycji
# (wykorzystując wcześniej napisaną metodę z klasy OrderElement) i wykorzystaj ją w konstruktorze
# do inicjalizacji łącznej wartości zamówienia.
from class_product import Product
class Order_Element:
    def __init__(self,product_information, amount):
        self.amount = amount
        self.product_information = product_information
    def print_self (self,):
        print(f"info:{self.product_information}, ilość {self.amount}")
    def calculate_position_prize(self, unit_prize):
        unit_prize = Product.prize
        return self.amount * unit_prize