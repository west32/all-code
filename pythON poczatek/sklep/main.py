# Napisz prosty symulator sklepu.
#
# W jednym pliku zdefiniuj dostępne produkty: nazwę (np. chleb i jabłka), dostępną ilość i cenę jednostkową.
# W innym zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości stworzy nowe
# zamówienie i doda je do listy zamówień. Zamówienie składa się z nazwy produktu, zamówionej ilości i łącznej ceny.
# Obydwa pliki umieść w pakiecie.
#
# Sklep uruchom poprzez plik main, w którym zaimportujesz funkcje do tworzenia zamówienia, wczytasz
# dane od użytkownika i wypiszesz łączny koszt zakupów. Zastosuj importowanie absolutne postaci from … import.

from sklep.shop import order_2

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