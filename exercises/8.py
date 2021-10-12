# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the
# lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c= []

def generate_the_list():
    list= []
    number_of_elements= random.randint(1,20)

    for _ in range (number_of_elements):
        element = random.randint(1, 100)
        list.append(element)
    return list
a= generate_the_list()
b= generate_the_list()
print(a)
print(b)

if len(a)> len(b):
    for number in a:
        if number in b and number not in c:
            c.append(number)
else:
    for number in b:
        if number in a and number not in c:
            c.append(number)
print(c)