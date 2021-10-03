def find_max(list):
    max_number = 0
    for number in list:
        if number > max_number:
            max_number = number
    return max_number