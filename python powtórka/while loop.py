# 1
# number= int(input("Podaj liczbę "))
# tries= 1
# while tries <10 and number %2 !=0:
#
#     number= int(input("podaj liczbe "))
#     tries += 1
#
# Wczytaj numer telefonu użytkownika i
# rozdziel go myślnikami (format XXX-XXX-XXX).

# 2
# number = input("podaj nr telefonu")
# number = number.replace("-", "")
# modified_number=""
# digit_index=0
# while digit_index < len(number):
#     if digit_index %3==0 and digit_index !=0:
#         modified_number += "-"
#     modified_number += number[digit_index]
#     digit_index += 1
#
# print(f"Twoj nr telefonu to {modified_number}")

# 3
# Poproś użytkownika o podanie ulubionych dań,
# ozdzielając każde z nich przecinkiem.
#
# Następnie wypisz każde z nich wraz z informacją, które miejsce
# zajmuje na jej/jego liście.

dishes= input("podaj dania rozdzielając je przecinkiem ").split(",")

index = 0

while index +1 <= len(dishes):
    print(f"{dishes[index]}-{index +1}")
    index +=1