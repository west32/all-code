# Utwórz klasę TaxCalculator z metodą statyczną obliczającą wartość podatku dla danej
# pozycji z zamówieniu (procent przemnożony przez wartość pozycji).
#
# Przyjmij następujące stawki podatkowe - w zależności od nazwy kategorii, do której należy produkt:
#
# 5% - “Owoce i warzywa”
# 8% - “Jedzenie”
# 20% - Wszystkie pozostałe kategorie

from shop.class_Order_element import OrderElement
from shop.class_order import Order
from shop.class_product import Product

class Tax_calculator:

    FRUITS_AND_VEGETABLES_TAX= 0.05
    FOOD_TAX = 0.08
    OTHERS = 0.2

    @staticmethod
    def calculate_with_tax(order_element):
        product_category = order_element.product.category
        if order_element.product.category == "jedzenie":
            tax_rate= Tax_calculator.FOOD_TAX
        elif order_element.product.category == "warzywa i owoce":
            tax_rate = Tax_calculator.FRUITS_AND_VEGETABLES_TAX
        else:
            tax_rate = Tax_calculator.OTHERS
        return tax_rate * order_element.calculate_position_prize()


