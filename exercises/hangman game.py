import random
from random_word_from_file import pick_random_word_from_data
from guess_the_letter import guessing_logic

def run_game():
   secret_word= pick_random_word_from_data("sowpods.txt")
   guessing_logic(secret_word)

if __name__=="__main__":
    run_game()