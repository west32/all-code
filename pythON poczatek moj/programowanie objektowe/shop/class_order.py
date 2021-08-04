# dwa zamówienia są równe jeżeli zostały złożone przez tego samego klienta, mają taką samą
# liczbę pozycji i są one sobie równe (nie muszą znajdować się na tych samych miejscach na liście)
import random
from shop.class_product import Product
from shop.class_Order_element import OrderElement


class Order:
    def __init__(self,orderer_first_name, orderer_last_name,_order_elements=None):
        if _order_elements is None:
            _order_elements = []
        self._order_elements = _order_elements
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        self._total_prize = self.calculate_order_prize()

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.orderer_first_name != other.orderer_first_name or self.orderer_last_name != other.orderer_last_name:
            return False
        if len(self._order_elements) != len(other._order_elements):
            return False
        for _order_elemenets in self._order_elements:
            if _order_elemenets not in other._order_elements:
                return False
        return True

    def calculate_order_prize(self):
            _total_prize = 0
            for element in self._order_elements:
                _total_prize += element.calculate_position_prize()
            return _total_prize
    def __str__(self):
        gap_between = 20*"="
        orderer = f"zamówienie dla : {self.orderer_first_name} {self.orderer_last_name}"
        total = f"łączna kwota do zapłaty to: {self._total_prize} PLN"
        products = "zamówione produkty:\n"
        for element in self._order_elements:
           products += f" \t {element}\n"
        result =  f"\n".join((gap_between, orderer, total,  products, gap_between))
        return result
    def __len__(self):
        return len(self._order_elements)
    def add_product(self,product,quantity):
        self._order_elements.append(OrderElement(product,quantity))
        self._total_prize = self.calculate_order_prize()

def generate_an_order():
    number_of_products= random.randint(1,5)
    _order_elements = []
    for product_number in range (number_of_products):
        product_name = f"Product- {product_number}"
        product_category = "inne"
        product_prize = random.randint(1,30)
        product = Product (product_name,product_category,product_prize)
        amount = random.randint(1, 5)

        _order_elements.append(OrderElement(product, amount))
    order = Order("Bartłomiej", "Juda", _order_elements)

    return order