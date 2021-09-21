import random
from dataclasses import dataclass
from shop.class_product import Product



@dataclass()
class OrderElement:
    product: Product
    quantity : float

    @staticmethod
    def orderelement_from_csv(name, category, quantity, price):
        identifier = random.randint(1, 9999)
        product = Product(name, category, price, identifier)
        quantity= quantity
        order_element=OrderElement(product,quantity)
        return order_element




    def calculate_position_prize(self):
        return self.quantity * self.product.price


    def __str__(self):

        return f"{self.product} x {self.quantity}"


















    # def print_self (self,):
    #     self.product.print_self()
    #     print(f"\t\t x {self.amount}")



