# Napisz metodę obliczającą łączną cenę jabłek, dla konkretnego obiektu Apple oraz łączną
# cenę ziemniaków dla konkretnego obiektu Potato
# na podstawie przekazanej w argumencie informacji o liczbie kilogramów.


class Apple :
    def __init__(self, species_name, size, prize_per_kg):
        self.size = size
        self.species_name = species_name
        self.prize_per_kg = prize_per_kg

    def count_total_apple_prize (self,amount):
        return   amount * self.prize_per_kg

