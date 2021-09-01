from dataclasses import dataclass
from enum import Enum

class ProductCategory (Enum):
    FOOD = "Jedznie"
    OTHERS = "Inne "


@dataclass
class  Product:
    name : str
    category : ProductCategory
    price : float

    def __str__(self):
        return f"Product: {self.name}    |Kategoria: {self.category.value}     |cena: {self.price}"

@dataclass
class ExpiringProduct(Product) :
    made_year : int
    years_fresh : int

    # def __init__(self,name,category,prize,made_year,years_fresh):
    #     super().__init__(name,category,prize)
    #     self.years_fresh = years_fresh
    #     self.made_year = made_year

    def does_expire(self,actual_year):
        return actual_year - self.made_year < self.years_fresh



