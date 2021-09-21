import os
import csv
from shop.store import AvailableProduct,ProductCategory


def update_available_products(available_products, file_name="available_products.csv"):
    with open (file_name, mode="w",newline="",encoding= 'utf-8') as available_products_file:
        csv_writer = csv.writer(available_products_file)
        csv_writer.writerow(["name","category","unit_price","identifier","quantity"])
        for  available_product in available_products:
            product = available_product.product
            csv_writer.writerow([product.name, product.category.name, product.price, product.identifier, available_product.quantity]
                                )



def load_available_products(file_name="available_products.csv"):
    with open(file_name,newline="",encoding="utf-8")as available_file:
        csv_reader= csv.reader(available_file)
        next(csv_reader)
        return [ AvailableProduct(
            name =row[0],
            category=ProductCategory[row[1]],
            unit_price=float(row[2]),
            identifier=int(row[3]),
            quantity=int(row[4]),
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