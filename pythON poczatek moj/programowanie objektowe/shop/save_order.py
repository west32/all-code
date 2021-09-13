import os

def save_order(order):
    order_data_path = os.path.join("data", "order.txt")
    with open(order_data_path,mode="a",encoding='utf-8') as order_file:
        order_file.write(str(order))
        order_file.write("\n")