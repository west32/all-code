class  Product:
    def __init__(self,name,category,prize):
        self.name = name
        self.category = category
        self.prize = prize

def print_product (product):
    print(f"Product: {product.name}    |Kategoria: {product.category}     |cena: {product.prize}")