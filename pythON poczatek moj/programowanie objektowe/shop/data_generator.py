import random
from shop.class_order import Order
from shop.class_product import Product
from shop.class_Order_element import OrderElement

def generate_an_order_elements (number_of_products= None):
    if number_of_products is None:
        number_of_products = random.randint (1,Order.MAX_ORDER_ELEMENTS)


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