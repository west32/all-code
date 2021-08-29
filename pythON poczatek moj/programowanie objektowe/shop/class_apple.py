# Stwórz odpowiednik klasy Apple jako named tuple.
#
#
# Stwórz instancję takiej krotki, a następnie wypisz zawarte w niej dane na trzy sposoby:
#
# korzystając z nazw
# odwołując się do kolejnych indeksów
# za pomocą pętli



class Apple :
    def __init__(self, species_name, size, price_per_kg):
        self.size = size
        self.species_name = species_name
        self.prize_per_kg = price_per_kg
    def __repr__(self):
        return f"<species_name= {self.species_name} size= {self.size} prize_per_kg= {self.prize_per_kg}>"
    def count_total_apple_prize (self,amount):
        return   amount * self.prize_per_kg

