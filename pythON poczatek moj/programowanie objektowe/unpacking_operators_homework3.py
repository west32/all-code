# Wygeneruj dwie listy zawierające losowe liczby całkowite i połącz je w jedną wykorzystując operator *.
#
# def combine_lists (one,other):
#     return one + other
import random

def generate_list():
    list=[]
    number_of_numbers = random.randint(4,10)
    for number in range(number_of_numbers):
        number = random.randint(1,50)
        list.append(number)
    return list
# LUB

def generate_list_by_mikolaj():
    result = []
    for _ in range (random.randint(5,10)):
        result.append(random.randint(1,100))
def run_homework():

    fist_list = generate_list()
    second_list = generate_list()
    two_lists = [*fist_list, *second_list]
    # two_lists= combine_lists(fist_list,second_list)
    print(two_lists)

if __name__=="__main__":
    run_homework()