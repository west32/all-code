# Zadanie nr 4
# Utwórz dwa słowniki i połącz je w jeden wykorzystując operator **.
#
# Tak otrzymany słownik “rozpakuj” wywołując funkcję z zadania drugiego.
from unpacking_op_homework2 import print_function
def run_homework():

    first_dict= {
        "zwierze" : "unicorn",
        "czlowiek" : "miszka",
        "miszka" : "unicorn"
    }

    second_dict = {
        "unicorn" : 300,
        "kotki": 2500,
        "miszka": 3000
}

    two_dicts = {**first_dict,**second_dict}
    # print(two_dicts)


    print_function(**two_dicts)

if __name__=="__main__":
    run_homework()