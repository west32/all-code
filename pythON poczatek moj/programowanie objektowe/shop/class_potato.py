# Napisz metodę obliczającą łączną cenę jabłek, dla konkretnego obiektu Apple oraz łączną
# cenę ziemniaków dla konkretnego obiektu Potato
# na podstawie przekazanej w argumencie informacji o liczbie kilogramów.
from dataclasses import dataclass

@dataclass()
class Potato :
   species_name = str
   size = str
   price_per_kg = float


   def count_total_potato_prize(self, amount):
       return amount * self.price_per_kg



