# Do klasy Order dodaj property typu setter, które będzie ustawiać listę pozycji w
# zamówieniu oraz aktualizować
# łączną wartość zamówienia (obliczaną na podstawie nowej listy pozycji).
#
# W setterze sprawdź również czy nowa lista elementów nie przekracza dopuszczalnej
# dla zamówienia ilości. Jeżeli
# przekracza, to przypisz do zamówienia tylko tyle pierwszych elementów z nowej listy,
# ile wynosi maksymalna dopuszczalna
# wartość w zamówieniu.

from shop.class_Order_element import OrderElement
from shop.discount_policy import standart_policy
from shop.data_generator import MAX_ORDER_ELEMENTS


class Order:

    # MAX_ORDER_ELEMENTS = 5

    def __init__(self, orderer_first_name, orderer_last_name, order_elements=None, discount_policy=None):
        if order_elements is None:
            order_elements = []
        self._order_elements = order_elements
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        if discount_policy is None:
            discount_policy= standart_policy
        self.discount_policy = discount_policy


    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self,value):
        if len(value) < MAX_ORDER_ELEMENTS:
            self._order_elements = value
        else:
            self._order_elements = value[:MAX_ORDER_ELEMENTS]




    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.orderer_first_name != other.orderer_first_name or self.orderer_last_name != other.orderer_last_name:
            return False
        if len(self.order_elements) != len(other.order_elements):
            return False
        for order_elemenets in self._order_elements:
            if order_elemenets not in other.order_elements:
                return False
        return True


    @property
    def total_price(self):
            total_price = 0
            for element in self._order_elements:
                total_price += element.calculate_position_prize()
            return self.discount_policy(total_price)


    def __str__(self):
        gap_between = 20*"="
        orderer = f"zamówienie dla : {self.orderer_first_name} {self.orderer_last_name}"
        total = f"łączna kwota do zapłaty to: {self.total_price} PLN"
        products = "zamówione produkty:\n"
        for element in self.order_elements:
           products += f" \t {element}\n"
        result =  f"\n".join((gap_between, orderer, total,  products, gap_between))
        return result
    def __len__(self):
        return len(self.order_elements)
    def add_product(self,product,quantity):
        if len(self.order_elements)>= MAX_ORDER_ELEMENTS:
            print("przykro nie ma juz wolnych miejsc w zamowieniu")
        else:
            new_element= OrderElement(product,quantity)
            self.order_elements.append(new_element)
            self.total_prize = self._calculate_order_prize()





