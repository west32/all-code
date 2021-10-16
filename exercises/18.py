import random


random_list= [random.randint(0,100) for number in range (0,20)]


def is_that_number_in_list(list):
    number=int(input("is this number in list? : "))
    return print(f"{number in list}")

print(random_list)
is_that_number_in_list(random_list)