import os
import csv
from shop.store import AvailableProduct,ProductCategory
import dataclasses

import json
from shop.class_order import Order,OrderElement



def save_order_in_json_file(order,file_name= "orders.json"):
    order_data={
            "orders":
                [
                    { "first_name": order.orderer_first_name,
                      "last_name": order.orderer_last_name,
                      "zamówione produkty:":",".join([dataclasses.asdict(order_element)])

                    }
                ]
        }

    with open (file_name,mode="w",) as order_file:




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