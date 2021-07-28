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

class OrderElement:
    def __init__(self,product, amount):
        self.amount = amount
        self.product = product
    def calculate_position_prize(self,):
        return self.amount * self.product.prize
    def print_self (self,):
        self.product.print_self()
        print(f"\t\t x {self.amount}")

class Chujtam:
    def __init__(self,chuj,dupa):
        self.dupa = dupa
        self.chuj = chuj
    def print_self(self):
        self.dupa.print_self()
        print(f"{self.chuj}")
def example():
    dupachuj= Chujtam ("maly", "duza")
    dupachuj.print_self()

example()