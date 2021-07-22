products = {
    "jabłka": {"prize": 1.2,
               "quantity": 200},
    "banany": {"prize": 1.5,
               "quantity": 100},
    "marchew": {"prize":0.5,
                "quantity": 300}}

def update_stock(product_name,quantity):
    products[product_name]['quantity']-=quantity

def is_product_on_list (name_of_product):
    for product in products:
        if product == name_of_product:
            result=True
            break
        else:
            result= False
    return result

