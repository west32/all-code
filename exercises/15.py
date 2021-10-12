# # Write a program (function!) that takes a list and returns a new list that contains all the elements
# # of the first list minus all the duplicates.
# #
# # Extras:
# #
# # Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# # Go back and do Exercise 5 using sets, and write the solution for that in a different function.
import random
#
#
def generate_list():
    # number_of_elements = random.randint(5, 20)
    # list = []
    #
    # for _ in range(number_of_elements):
    #     number = random.randint(1, 20)
    #     list.append(number)
    list = [random.randint(0, 20) for _ in range(40)]
    return list


list = generate_list()
print(list)

def no_duplicates_loop(list):
    a = list
    b=[]
    for number in a:
        if number not in b:
            b.append(number)
    return b

def no_duplicates_set(list):
    list= set(list)
    list_no_duplicates= [number for number in list]
    return list_no_duplicates

print(no_duplicates_loop(list))
print(no_duplicates_set(list))

