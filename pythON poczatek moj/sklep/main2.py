from shop2.order import make_new_order,orders_list
from shop2.product_store import is_product_on_list

def run_the_shop():

    print("Witaj w sklepie")
    name_of_product=None
    while name_of_product != 'x':
        name_of_product = input("Wybierz produkt,aby przerwać wciśnij 'x'")
        if is_product_on_list(name_of_product) is False:
            print(f"Przykro na nie posiadamy {name_of_product} w sklepie")
        else:
            number_of_product= int(input(f"jaka ilość {name_of_product}"))
            make_new_order(name_of_product,number_of_product)
    full_prize= 0
    for index,prize in enumerate(orders_list):
        full_prize += orders_list[index]['prize']
    print(f"Łączna kwota zamówienia to: {full_prize}")

if __name__ == '__main__':
    run_the_shop()