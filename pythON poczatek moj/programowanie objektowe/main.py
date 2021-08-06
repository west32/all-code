# Wygeneruj 5 losowych zamówień i posortuj je rosnąco po ich łącznej cenie.
#
# Zastosuj własną funkcję zwracającą odpowiednią wartość, która będzie używana do porównania przez funkcję sortującą.

from shop.class_product import Product
from shop.class_Order_element import OrderElement
from shop.class_order import Order
from shop.class_tax_caculator import Tax_calculator

def run_homework ():

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
if __name__ == '__main__':
    run_homework()