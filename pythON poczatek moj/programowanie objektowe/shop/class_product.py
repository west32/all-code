class  Product:
    def __init__(self,name,category,prize):
        self.name = name
        self.category = category
        self.prize = prize

    def print_self (self):
        print(f"Product: {self.name}    |Kategoria: {self.category}     |cena: {self.prize}")

