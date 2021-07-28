import random
from shop.class_product import Product
from shop.class_Order_element import OrderElement


class Order:
    def __init__(self,orderer_first_name, orderer_last_name,order_elements=None):
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        self.total_prize = self.calculate_order_prize()

    def calculate_order_prize(self):
            total_prize = 0
            for element in self.order_elements:
                total_prize += element.calculate_position_prize()
                return total_prize



    def print_self (self):
        print(20*"=")
        print(f"zamówienie dla : {self.orderer_first_name} {self.orderer_last_name}")
        print("zamówione produkty:")
        for product in self.order_elements:
            print("\t", end="")
            product.print_self()
        print(f"łączna kwota do zapłaty to: {self.total_prize} PLN")
        print(20 * "=")
        print()
def generate_an_order():
    number_of_products= random.randint(1,20)
    order_elements = []
    for product_number in range (number_of_products):
        product_name = f"Product- {product_number}"
        product_category = "inne"
        product_prize = random.randint(1,30)
        product = Product (product_name,product_category,product_prize)
        order_elements.append(product)
        amount = random.randint(1,5)
        order_elements.append(OrderElement(product, amount))
    order = Order("Bartłomiej", "Juda", order_elements)

    return order