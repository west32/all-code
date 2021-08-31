# Stwórz enuma reprezentującego kategorię produktu.
#
# Poszczególnym elementom nadaj odpowiednie nazwy (np. FOOD), zaś jako wartość podaj tekst,
# który ma być traktowany jako “wypisywalna” nazwa kategorii (np. “Jedzenie”).
#
# Zastąp nazwę kategorii w produkcie - kategorią (enumem).
#
# Dostosuj odpowiednio metodę generującą pozycje w zamówieniu i wypisującą produkt.


from dataclasses import dataclass
from enum import Enum



class  Product(Enum):
    name: str
    category: str
    price : float


    def __str__(self):
        return f"Product: {self.name}    |Kategoria: {self.category}     |cena: {self.price}"

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



