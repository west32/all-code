# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order, Apple i Potato:
#
# Product: nazwa, nazwa kategorii, cena jednostkowa
# Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena
# (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
# Apple: nazwa gatunku, rozmiar, cena za kg
# Potato: nazwa gatunku, rozmiar, cena za kg
# Utwórz kilka obiektów każdej klasy.

class Product:
    def __init__(self,name,category_name,prize):
        self.name = name
        self.category_name = category_name
        self.prize = prize
class  Order:
    def __init__(self,orderer_first_name,orderer_last_name,total_prize,produts_list=None):
        self.orderer_first_name = orderer_first_name
        total_prize= calculate_total_prize(produts_list)
        self.total_prize = calculate_total_prize(produts_list)
        self.orderer_last_name = orderer_last_name
        if produts_list is None:
            produts_list = []
        self.product.list = produts_list

def calculate_total_prize(products_list):
    for Product in products_list:
        total_prize=0
        total_prize += Product.prize
        return total_prize


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

Piotr_order= Order("Piotr","Sochacki",total_p)
