from shop.class_product import Product
from main import run_homework


first_list = [Product(name="cookie",category="food",prize=4), Product(name="shoes", category="wear", prize=45)]
second_list = ["obiad","sniadanie","kolacja","piwo"]

for element in first_list:
    second_list.append(element)
    print (second_list)

print(first_list)
print(second_list)