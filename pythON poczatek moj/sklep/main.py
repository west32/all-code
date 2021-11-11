# Zadanie nr 1
# Utwórz “ręcznie” plik csv zawierający informacje o dostępnych produktach.
#
# Wykorzystaj csv.reader i napisz funkcję “ładującą” stan magazynu z pliku csv.
#
# Uruchamiaj ją za każdym razem przy starcie programu.

# from sklep.shop import order_2
from shop import order_2
name_of_product = None
while name_of_product != 'x':

    name_of_product=input("co chcesz zamówić? wcisnij 'x' aby przerwać")
    if name_of_product =='x':
        break
    elif order_2.is_product_on_list(name_of_product)is False:
        print("przykro nam, nie mamy podanego produktu w sprzedaży")
    else:
        number_of_product_input = input(f"jaką ilość {name_of_product} chcesz zamówić?")
        number_of_product=int(number_of_product_input)
        order_2.make_an_order(name_of_product,number_of_product)
        print(f"oto Twoja lista zakupów{order_2.order_list}")
total_prize= 0
for index,product in enumerate(order_2.order_list):

    total_prize += order_2.order_list[index]['total_prize']
print(f"suma Twojego zamowienia {total_prize}pln")