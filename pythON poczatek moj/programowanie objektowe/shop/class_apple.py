from dataclasses import dataclass
# Stwórz odpowiednik klasy Apple jako named tuple.
#
#
# Stwórz instancję takiej krotki, a następnie wypisz zawarte w niej dane na trzy sposoby:
#
# korzystając z nazw
# odwołując się do kolejnych indeksów
# za pomocą pętli


@dataclass
class Apple :
   size : str
   species_name : str
   price_per_kg : float


   def count_total_apple_prize(self, quantity):
       return quantity * self.price_per_kg




# def __init__(self, species_name, size, price_per_kg):
#     self.size = size
#     self.species_name = species_name
#     self.prize_per_kg = price_per_kg


