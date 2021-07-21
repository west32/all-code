# W innym zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości stworzy nowe
# zamówienie i doda je do listy zamówień. Zamówienie składa się z nazwy produktu, zamówionej ilości i łącznej ceny.


from sklep.shop import stock
order_list=[]
def make_an_order(name_of_product,number_of_product,):

        if number_of_product > stock.products[name_of_product]['dostepność']:
            print(f"przepraszamy pozostało tylko {name_of_product}:{stock.products[name_of_product]['dostepność']} zamawianego produktu ")
        else:
            prize_for_single=stock.products[name_of_product]['cena_za_sztuke']
            total_prize = number_of_product * prize_for_single
            order = {name_of_product: {"number_of_product": number_of_product,
                                       "total_prize": total_prize}}
            order_list.append(order)
            return order_list


name_of_product=None
def is_product_on_list(name_of_product):
    for product in stock.products:
        if product == name_of_product:
            result=True
            break
        else:
            result= False
    return result

