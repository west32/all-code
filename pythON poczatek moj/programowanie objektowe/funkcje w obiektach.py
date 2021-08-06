import random

# pierwsza funkcja
def say_hello():
    print("Hello World!")
# druga funkcja
def say_good_bye():
    print("Good bye!")
# trzecia ktora za argumenty przyjmuje pierwsza i druga i losuje ktora zwrocic
def randomize_func(first_func, second_func):
    number = random.randint (1,2)
    if number == 1:
        return first_func
    return second_func

def run_exmple():
    hello_or_good_bye=randomize_func(say_hello,say_good_bye)
    hello_or_good_bye()

if __name__ == '__main__':
    run_exmple()