
# metoda clear usuwa wszystkie elementy z listy
# print(favourite_falvours)
# favourite_falvours.clear()
# print(favourite_falvours)

# print(favourite_falvours)
# favourite_falvours.reverse()
# print(favourite_falvours)


# print(favourite_falvours.count("malinowy"))


# copy_of_flavours = favourite_falvours.copy()
# print(copy_of_flavours)

# new_flavours = ["orzechowy", "jagodowy"] * 4
# favourite_falvours.extend(new_flavours)
# favourite_falvours += new_flavours


# print(new_flavours)



# print(numbers[:4])
# print(numbers[8:])
# copy_numbers= numbers[:]
# print(numbers[2::3])

# numbers = []
# for number in range (15):
#     if number %2==0:
#         numbers.append(number)

# numbers = [number for number in range (15) if number % 2 ==0]
# print(numbers)

# favourite_falvours = [
#     "malinowy",
#     "truskawkowy",
#     "czekoladowy",
#     "pistacjowy",
#     "kokosowy",

# flavours = [flavour for index, flavour in enumerate(favourite_falvours) if index %2==0]
# print(flavours)

# flavours = [flavour if index %2==0 else "---" for index,flavour in enumerate(favourite_falvours)]
# print(flavours)
# flavours= []
# for index, flavour in enumerate(favourite_falvours):
#     if index %2 == 0:
#         flavours.append(flavour)
#     else:
#         flavours.append("---")
# print(flavours)

# rows_and_cols = [[row for row in range(5)] for column in range(4)]
# print(rows_and_cols)

# rows_and_cols= []
# for column in range (4):
#     rows_and_cols.append([])
#     for rows in range (5):
#         rows_and_cols[column].append(rows)
# print(rows_and_cols)

# Używając list comprehensions wygeneruj listy zawierające
# liczby od 1 do 30 podzielne kolejno przez 3 oraz przez 5.
#
# To znaczy, że na pierwszej liście powinny znaleźć się
# liczby od 1 do 30 podzielne przez 3, a na drugiej liście liczby od 1 do 30 podzielne przez 5.
#
# Następnie, połącz obie listy w jedną i wypisz wynik.

# Zadanie nr 2
# Wczytaj od użytkownika listę ulubionych sportów, a następnie stosując slicing wypisz co drugi, pomijając
# pierwszy sport z listy.

def run_homework():

    # numbers_one = [number for number in range (1,31) if number %3==0]
    # print(numbers_one)
    # numbers_two =[number for number in range (1,31) if number %5==0]
    # print(numbers_two)
    #
    # numbers_one.extend(numbers_two)
    # print(numbers_one)


    favourite_sports_input = input("wypisz swoje ulubione sporty oddzielając je przycinkiem").split(",")

    favourite_sports= [sport for sport in favourite_sports_input]


    print(favourite_sports [1::2])


if __name__=="__main__":
    run_homework()