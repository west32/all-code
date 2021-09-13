import os

def save_order(order):
    order_data_path = os.path.join("data", "order.txt")
    with open(order_data_path,mode="a",encoding='utf-8') as order_file:
        order_file.write(str(order))
        order_file.write("\n")

def load_orders():
    order_data_path = os.path.join("data", "order.txt")
    with open(order_data_path, mode="r") as order_data_file:
        order_data = order_data_file.read()
        print("Oto Twoje zamówienia")
        return order_data