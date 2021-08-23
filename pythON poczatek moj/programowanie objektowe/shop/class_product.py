# Do klasy Product dodaj pole identifier, będące liczbą.
#
# Następnie, zaktualizuj generator pozycji zamówienia, tak
# aby generował produkty zawierające losowy identyfikator.
#
# Użyj dict comprehensions, aby zamienić listę pozycji zamówienia w
# słownik, gdzie kluczem będzie identyfikator produktu z danej pozycji,
# a wartością będzie dany obiekt klasy Product.


class  Product:
    def __init__(self,name,category,prize,identifier):
        self.identifier = identifier
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

class ExpiringProduct(Product) :
    def __init__(self,name,category,prize,made_year,years_fresh):
        super().__init__(name,category,prize)
        self.years_fresh = years_fresh
        self.made_year = made_year

    def does_expire(self,actual_year):
        return actual_year - self.made_year < self.years_fresh