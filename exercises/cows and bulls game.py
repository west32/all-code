import random

def welcome():
    name= input("What's your name? >>>")
    print(f"{name} Welcome to the Cows and Bulls game!")

def generate_secret_number():
    secret_number = ""
    for _ in range (4):
        number= random.randint(0,9)
        secret_number += str(number)
    return secret_number

def game (secret_number, name):
    number_of_tries= 0
    while True:
        number_of_tries +=1
        guess = input(str(""" Enter 4-digits number
>>>"""))
        number_of_cows= 0
        number_of_bulls=0
        for index,element in enumerate(guess):
            if element[index] == element[index] in secret_number:
                number_of_cows +=1
            elif element in secret_number:
                number_of_bulls +=1
            elif guess == secret_number:
                if number_of_tries == 1:
                    print(f"Conratulation {name}, your answer correctly in 1st try! the number it's {secret_number}")
                else:
                    print (f"Conratulation {name}, your answer correctly in {number_of_tries} tries! the number it's {secret_number}")
                break

def run_game():
    name= welcome()
    secret_number= generate_secret_number()
    print(secret_number)
    game(secret_number,name)

if __name__=="__main__":
    run_game()