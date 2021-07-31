# Zaimplementuj metodę __str__ dla klas Order, OrderElement oraz Product (zastępując dotychczasową print_self).
# dwa produkty są równe jeżeli mają taką samą nazwę, kategorię i cenę jednostkową
class  Product:
    def __init__(self,name,category,prize):
        self.name = name
        self.category = category
        self.prize = prize
    def __eq__(self, other):
        if self.__class__!=other.__class__:
            return NotImplemented
        return (self.name == other.name and
        self.category == other.category and
        self.prize == other.prize)
    def __str__(self):
        return f"Product: {self.name}    |Kategoria: {self.category}     |cena: {self.prize}"
