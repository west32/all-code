from dataclasses import dataclass
from shop.class_product import Product

@dataclass()
class OrderElement:
    quantity = float
    product = Product
    # def __init__(self,product, quantity):
    #     self.quantity = quantity
    #     self.product = product

    def calculate_position_prize(self):
        return self.quantity * self.product.price



    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented

        return  self.product == other.product and self.quantity == other.quantity

    def __str__(self):

        return f"{self.product} x {self.quantity}"


















    # def print_self (self,):
    #     self.product.print_self()
    #     print(f"\t\t x {self.amount}")



