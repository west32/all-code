from shop.class_product import Product
from shop.class_Order_element import OrderElement
from shop.class_order import Order, generate_an_order

def run_homework ():

    # green_apple = Apple (species_name="green",size="small",prize_per_kg=3)
    # red_apple = Apple (species_name="red", size="bif", prize_per_kg=5)
    # print(green_apple)
    # print(red_apple)

    # first_order= generate_an_order()
    # print (first_order)
    # second_order = generate_an_order()
    # print(second_order)

    cookie = Product (name= "cookie", category="food", prize=3)
    shoes = Product (name="rebook", category="clothes", prize=35)

    first_order_elements =[ OrderElement (product=cookie, quantity=36) , OrderElement(product=shoes, quantity=3),  ]
    second_order_elements = [OrderElement(product=cookie, quantity=3), OrderElement(product=shoes, quantity=39)]
    first_order = Order (orderer_first_name="Bartek", orderer_last_name="Juda", order_elements= first_order_elements)
    second_order = Order(orderer_first_name="Bartek", orderer_last_name="Juda", order_elements= second_order_elements)
    if first_order == second_order:
        return print("Te zamówienia są równe")
    else:
        print ("nie są równe")

if __name__ == '__main__':
    run_homework()