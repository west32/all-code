# Dodaj do klasy Order maksymalną dopuszczalną liczbę elementów w zamówieniu.
#
# Upewnij się, że nie zostaje ona przekroczona podczas tworzenia obiektu klasy
# Order (w konstruktorze - gdy przekracza stwórz zamówienie tylko z pierwszymi X elementami)
# i podczas dodawania nowego produktu do zamówienia (gdy przekracza nie dodawaj produktu do
# zamówienia tylko wypisz informacje o przekroczeniu limitu).
#
# Żeby kontrolować liczbę pozycji w generowanym zamówieniu zastąp losową liczbę pozycji
# argumentem przekazanym do generate_order.
import random
from shop.class_product import Product
from shop.class_Order_element import OrderElement


class Order:

    MAX_ORDER_ELEMENTS = 5
    def __init__(self, orderer_first_name, orderer_last_name, order_elements=None):
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            order_elements = order_elements [:Order.MAX_ORDER_ELEMENTS]
        self.order_elements = order_elements
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        self._total_prize = self.calculate_order_prize()

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.orderer_first_name != other.orderer_first_name or self.orderer_last_name != other.orderer_last_name:
            return False
        if len(self.order_elements) != len(other.order_elements):
            return False
        for order_elemenets in self.order_elements:
            if order_elemenets not in other.order_elements:
                return False
        return True

    def calculate_order_prize(self):
            _total_prize = 0
            for element in self.order_elements:
                _total_prize += element.calculate_position_prize()
            return _total_prize
    def total_prize_to_sort(self):
        self._total_prize
    def __str__(self):
        gap_between = 20*"="
        orderer = f"zamówienie dla : {self.orderer_first_name} {self.orderer_last_name}"
        total = f"łączna kwota do zapłaty to: {self._total_prize} PLN"
        products = "zamówione produkty:\n"
        for element in self.order_elements:
           products += f" \t {element}\n"
        result =  f"\n".join((gap_between, orderer, total,  products, gap_between))
        return result
    def __len__(self):
        return len(self.order_elements)
    def add_product(self,product,quantity):
        if len(self.order_elements)>= Order.MAX_ORDER_ELEMENTS:
            print("przykro nie ma juz wolnych miejsc w zamowieniu")
        else:
            new_element= OrderElement(product,quantity)
            self.order_elements.append(new_element)
            self._total_prize = self.calculate_order_prize()
    @classmethod
    def generate_an_order(cls,number_of_products):
        order_elements = []
        for product_number in range (number_of_products):
            product_name = f"Product- {product_number}"
            product_category = "inne"
            product_prize = random.randint(1,30)
            product = Product (product_name,product_category,product_prize)
            amount = random.randint(1, 5)
            order_elements.append(OrderElement(product, amount))

        order = Order("Bartłomiej", "Juda", order_elements)
        return order