def change_into_range(number,range=0.1):
    lower_border = number-(number*range)
    higher_border = number+(number*range)

    return lower_border,higher_border


print(change_into_range(100))
print(change_into_range(100,0.3))