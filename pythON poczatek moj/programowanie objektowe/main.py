# Wygeneruj 5 losowych zamówień i posortuj je rosnąco po ich łącznej cenie.
#
# Zastosuj własną funkcję zwracającą odpowiednią wartość, która będzie używana do porównania przez funkcję sortującą.
import random

from shop.class_product import Product,ExpiringProduct
from shop.class_Order_element import OrderElement
from shop.class_order import Order
from shop.class_ExpressOrder import ExpressOrder
from shop.class_tax_caculator import Tax_calculator
from shop.discount_policy import AbsoluteDiscount,DiscountPolicy,PercentageDiscount
from shop.data_generator import generate_order_elements


# def generate_order_elements():
#     order_elements = []
#     for product_number in range(1,5):
#         product_name = product_number
#         product_category = "inne"
#         product_prize = random.randint (1,10)
#         product= Product(product_name,product_category,product_prize)
#         product_quantity = random.randint(1,10)
#         order_elements.append(OrderElement(product,product_quantity))
#     return order_elements
#

# def generate_order_elements():
#     order_elements = []
#     for product_number in range(1, 6):
#         product_name = product_number
#         category = "inne"
#         prize = random.randint(3, 20)
#         product = Product(product_name, category, prize)
#         quantity = random.randint(1, 6)
#         order_element = OrderElement(product, quantity)
#         order_elements.append(order_element)
#     return order_elements
#
#
#
#
def run_homework():
    # mleko = ExpiringProduct(name="mleko",category="nabiał",prize=3,made_year=2020,years_fresh=3)
    # print(mleko.does_expire(actual_year=2021))

    first_name = "bartek"
    last_name = "Juda"
    order_elements = generate_order_elements()
    normal_order = Order(first_name, last_name, order_elements)
    percentage_discount= PercentageDiscount(discount_percentage=10)
    absolute_discount= AbsoluteDiscount(discount_amount=100)
    order_percent_discount = Order(first_name,last_name,order_elements,discount_policy=percentage_discount)
    order_absolute_discount = Order(first_name,last_name,order_elements,discount_policy=absolute_discount)
    print(normal_order)
    print(order_percent_discount)
    print(order_absolute_discount)
    #
    # new_elements = generate_order_elements(3)
    # normal_order.order_elements = new_elements
    # print(normal_order)
    #
    # too_many_elements = generate_order_elements(1000)
    # normal_order.order_elements = too_many_elements
    # print(normal_order)

    # print(order)
    # for element in order.order_elements:
    #     print (element)
    # standart_order = Order(first_name, last_name, order_elements)
    # loyal_order = Order(first_name, last_name, order_elements, discount_policy=loyal_policy)
    # christmas_order = Order(first_name, last_name, order_elements, discount_policy=christmas_policy)
    #
    # print(standart_order)
    # print(loyal_order)
    # print(christmas_order)

    # first_name= "Bartłomiej"
    # last_name = "Juda"
    # order_elements= generate_order_elements()
    # defoult_order= Order(first_name,last_name,order_elements,)
    # loyal_order = Order(first_name,last_name,order_elements,discount_policy=loyal_policy)
    # christmas_order= Order(first_name,last_name,order_elements,discount_policy=christmas_policy)
    #
    # print(defoult_order)
    # print(loyal_order)
    # print(christmas_order)


# def get_total_prize(order):
#     return order.total_prize

# def run_homework ():
#     orders_list= []
#     for _ in range(5):
#         orders_list.append(Order.generate_an_order())


if __name__ == "__main__":
    run_homework()

    # green_apple = Product (name="zielone jabłko", category="warzywa i owoce", prize=4)
    # red_apple = Product (name="czerwone jabłko", category="warzywa i owoce", prize=7)
    # shoes = Product (name="buty", category="inne", prize=350)
    # cookie = Product(name="cookie", category="jedzenie", prize=3)
    # five_red_apples = OrderElement(red_apple,quantity=5)
    # ten_cookies = OrderElement(cookie, quantity=10)
    # two_shoes = OrderElement(shoes,quantity=2)
    # green_apple_tax= Tax_calculator.calculate_with_tax(green_apple)
    # red_apple_tax = Tax_calculator.calculate_with_tax(red_apple)
    # shoes_tax = Tax_calculator.calculate_with_tax(shoes)
    # five_red_apples_tax = Tax_calculator.calculate_with_tax(five_red_apples)
    # ten_cookies_tax = Tax_calculator.calculate_with_tax(ten_cookies)
    # two_shoes_tax = Tax_calculator.calculate_with_tax(two_shoes)
    # print(ten_cookies.calculate_position_prize())
    # print(ten_cookies_tax)
    #
    # print (f" cena pary butów butów:{two_shoes.calculate_position_prize()} + podatek: {two_shoes_tax}")

    # order_over_limit = Order.generate_an_order(10)
    # print (order_over_limit)

    # order_below_limit = Order.generate_an_order(2)
    # order_below_limit.add_product(cookie,quantity=10)
    # print(order_below_limit)
    # order_over_limit.add_product(green_apple,quantity=8)
    # print(order_over_limit)
    # second_order = generate_an_order()
    # print(second_order)

    # shoes = Product (name="rebook", category="clothes", prize=35)

    # first_order_elements =[ OrderElement (product=cookie, quantity=3) , OrderElement(product=shoes, quantity=3),  ]
    # second_order_elements = [OrderElement(product=cookie, quantity=3), OrderElement(product=shoes, quantity=3)]
    # first_order = Order (orderer_first_name="Bartek", orderer_last_name="Juda", order_elements= first_order_elements)
    # second_order = Order(orderer_first_name="Bartek", orderer_last_name="Juda", order_elements= second_order_elements)
    # if first_order == second_order:
    #     return print("Te zamówienia są równe")
    # else:
    #     print ("nie są równe")
