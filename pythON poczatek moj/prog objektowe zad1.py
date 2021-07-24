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


    def add_product_to_list(product, products_list):
        Order.products_list.append(product)
    Orders= [Order(),Order(),Order(),Order(),Order()]

    Products = {
        "mleko": Product(),
        "banany": Product(),
        "białko": Product()
    }

    print(Orders)
    print(Products)