# Wylosuj 6 liczb typu float z przedziału od -20 do 20 oraz 3 liczby
# całkowite z przedziału od 1 do 10.
#
# Następnie na pierwszych trzech liczbach typu float zastosuj zaokrąglanie
# (kolejno round, ceil oraz floor).
#
# Kolejne trzy liczby typu float podnieś do potęgi o wartości odpowiednio
# pierwszej, drugiej i trzeciej wylosowanej liczby całkowitej.



import math
import random


def run_homework():

    float_numbers = []
    int_numbers = []

    for _ in range (6):
        float_number= random.uniform(-20,20)
        float_numbers.append(float_number)


    for _ in range (3):
        int_number = 0
        int_number = random.randint(1,10)
        int_numbers.append(int_number)



    print(float_numbers)
    print(int_numbers)

    print(round(float_numbers[0]))
    print(math.ceil(float_numbers[1]))
    print(math.floor(float_numbers[2]))

    print(float_numbers[3] ** int_numbers[0])
    print(pow(float_numbers[4] , int_numbers[1]))
    print(math.pow(float_numbers[5], int_numbers[2]))


if __name__ == "__main__":
    run_homework()