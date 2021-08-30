from dataclasses import dataclass

@dataclass()
class  Product:
    name= str
    category = str
    price = float
    # def __init__(self,name,category,prize):
    #
    #     self.name = name
    #     self.category = category
    #     self.prize = prize
    def __eq__(self, other):
        if self.__class__!=other.__class__:
            return NotImplemented
        return (self.name == other.name and
        self.category == other.category and
        self.price == other.prize)
    def __str__(self):
        return f"Product: {self.name}    |Kategoria: {self.category}     |cena: {self.price}"

@dataclass
class ExpiringProduct(Product) :
    made_year = int
    years_fresh = int

    # def __init__(self,name,category,prize,made_year,years_fresh):
    #     super().__init__(name,category,prize)
    #     self.years_fresh = years_fresh
    #     self.made_year = made_year

    def does_expire(self,actual_year):
        return actual_year - self.made_year < self.years_fresh



