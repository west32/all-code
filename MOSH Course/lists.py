lista = [2,5,234,54,1,35,54,12,3,523,34,3]

def find_max(list):
    max_number = 0
    for number in list:
        if number > max_number:
            max_number = number
    return max_number
# uniques = []
# for number in lista:
#     if number not in uniques:
#         uniques.append(number)
# print (uniques)


# lepiej krocej


# set_of_list= set(lista)
# lista = list(set_of_list)
# print()