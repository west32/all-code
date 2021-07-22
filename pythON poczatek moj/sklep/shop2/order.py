from .product_store import products, update_stock

orders_list= [
    {"product_name": "masło",
     "prize": 8,
     "quantity": 1}
]

def make_new_order (name_of_product,quantity):
    avaible_quantity= products[name_of_product]['quantity']
    prize = products[name_of_product]['prize']
    if avaible_quantity < quantity:
        print(f" przykro nam, w magazynie mamy tylko {name_of_product}: {products[name_of_product]['quantity']}")
        return None

    else:
        total_prize= prize * quantity
        new_order = {"name_of_product":name_of_product,
                     "quantity": quantity,
                     "prize": total_prize}
        orders_list.append(new_order)
        update_stock(name_of_product,quantity)
        print(f"Twoja lista zamówień: {orders_list}")

    return new_order
