# Stwórz klasę reprezentującą produkt z terminem ważności (dziedziczącą po klasie Product).
#
# Rozszerz implementację bazową o dodatkowe pola: rok produkcji oraz liczbę lat ważności i metodę does_expire.
#
# Metoda ta przyjmuje jako argument aktualny rok oraz sprawdza czy od daty produkcji do podanego roku minęła
# liczba lat większa od tej podanej jako lata ważności


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

class ExpiringProduct(Product) :
    def __init__(self,name,category,prize,made_year,years_fresh):
        super().__init__(name,category,prize)
        self.years_fresh = years_fresh
        self.made_year = made_year

    def does_expire(self,actual_year):
        return actual_year - self.made_year < self.years_fresh