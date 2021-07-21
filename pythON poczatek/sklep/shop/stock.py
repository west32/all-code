products = {
    "jabłka": {"cena_za_sztuke": 1.2,
               "dostepność": 200},
    "banany": {"cena_za_sztuke": 1.5,
               "dostepność": 100},
    "marchew": {"cena_za_sztuke":0.5,
                "dostepność": 300}}

def update_stock(product_name,dostepność_zamowienie):
    products[product_name]['dostepność']-=dostepność_zamowienie
