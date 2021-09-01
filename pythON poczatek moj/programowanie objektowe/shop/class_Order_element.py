from dataclasses import dataclass
from shop.class_product import Product

@dataclass()
class OrderElement:
    product: Product
    quantity : float



    def calculate_position_prize(self):
        return self.quantity * self.product.price


    def __str__(self):

        return f"{self.product} x {self.quantity}"


















    # def print_self (self,):
    #     self.product.print_self()
    #     print(f"\t\t x {self.amount}")



