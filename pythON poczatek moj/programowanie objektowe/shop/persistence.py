import os
import csv
from shop.store import AvailableProduct,ProductCategory
import dataclasses
from shop.class_product import Product
import json
from shop.class_order import Order,OrderElement



def save_order_in_json_file(order,file_name= "orders.json"):
    new_order_data={
        "first_name": order.orderer_first_name,
        "last_name": order.orderer_last_name,
        "order_elements:":[
            {
                "product":{
                    "name": order_element.product.name,
                    "category": order_element.product.category.name,
                    "unit_price": order_element.product.price,
                    "identifier": order_element.product.identifier
                },

                    "quantity":order_element.quantity
            }for order_element in order.order_elements

        ]}
    try:
        with open (file_name,mode="r",) as orders_file:
            orders_data= json.load(orders_file).get("orders",[])
    except FileNotFoundError:
        orders_data = []

    orders_data.append(new_order_data)
    with open (file_name,"w") as orders_file:
        json.dump({"orders": orders_data}, orders_file,indent=4)

def load_orders (client_first_name,client_last_name,file_name="orders.json"):
    try:
        with open(file_name,mode="r") as orders_file:
            orders_by_clients_data = json.load(orders_file).get("orders",{})
    except FileNotFoundError:
        orders_by_clients_data = {}

    client_id = f"{client_first_name}-{client_last_name}"
    if client_id not in orders_by_clients_data:
        return []
    orders = orders_by_clients_data[client_id]
    return [
        Order(
            orderer_first_name= order["client_first_name"],
            orderer_last_name= order["client_last_name"],
            order_elements=[OrderElement(
                quantity=order_element["quantity"],
                product= Product(
                    name=order_element["product"]["name"],
                    category=ProductCategory[order_element["product"]["category"]],
                    price=order_element["product"]["price"],
                    identifier=order_element["product"]["identifier"],
                )
            )for order_element in order["order_elements"]],

        )for order in orders
    ]


def update_available_products(available_products, file_name="available_products.csv"):
    with open (file_name, mode="w",newline="",encoding= 'utf-8') as available_products_file:
        headers = ["name", "category", "unit_price", "identifier", "quantity"]
        csv_writer = csv.DictWriter(available_products_file,fieldnames=headers)
        csv_writer.writeheader()

        for  available_product in available_products:
            product = available_product.product
            csv_writer.writerow({
                "name":product.name,
                "category":product.category.name,
                "unit_price":product.price,
                "identifier":product.identifier,
                "quantity":available_product.quantity}
                                )



def load_available_products(file_name="available_products.csv"):
    with open(file_name,newline="",encoding="utf-8")as available_file:
        csv_reader= csv.DictReader(available_file)
        return [
            AvailableProduct(
                name =row["name"],
                category=ProductCategory[row["category"]],
                unit_price=float(row["unit_price"]),
                identifier=int(row["identifier"]),
                quantity=int(row["quantity"]),
            )
            for row in csv_reader
        ]




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