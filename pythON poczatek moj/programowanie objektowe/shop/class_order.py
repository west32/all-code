import random
from shop.class_product import Product
from shop.class_order_element


class Order:
    def __init__(self,orderer_first_name, orderer_last_name,positions_list=None):
        if positions_list is None:
            positions_list_list = []
        self.positions_list = positions_list
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        # total_prize = 0
        # for product in positions_list:
        #     total_prize += product.prize
        # self.total_prize = total_prize



    def print_self (self):
        print(20*"=")
        print(f"zamówienie dla : {self.orderer_first_name} {self.orderer_last_name}")
        print("zamówione produkty:")
        for product in self.products_list:
            print("\t", end="")
            product.print_self()
        print(f"łączna kwota do zapłaty to: {self.total_prize} PLN")
        print(20 * "=")
        print()
def generate_an_order():
    number_of_products= random.randint(1,20)
    products= []
    for product_number in range (number_of_products):
        product_name= f"Product- {product_number}"
        product_category = "inne"
        product_prize = random.randint(1,30)
        product =  (product_name,product_category,product_prize)
        products.append(product)
    order = Order("Bartłomiej", "Juda",products)
    return order