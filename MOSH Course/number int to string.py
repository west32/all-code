numbers = {
    "1": "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"

}

# MOJ SPOSOB
input_digits = input("phone: ")
number = ""
for digit in input_digits:
    number += f" {numbers[int(digit)]}"
print(number)

# MOSHA sposob
phone = input("Phone: ")

output= ""
for charakter in phone:
    output += numbers.get(charakter,"!") +  " "
print(output)

# efekt ten sam :) a sposoby bardzo podobne TYlko mosha sposob
#  czyta klucze slownika jako stringi dlatego musza byc w cudzoslowiu
# jak "1" w sumie lepiej bo input i tak zbiera stringi przu okazji
# nie trzeb tego potem zamieniac na int jak w moim sposobie
#  kolejny plus jest taki ze funkcja get pozawala okrslic znak
#  ktory bedzie wyswietlony gdyby uzytkownik wpisal znak z poza list
# kluczy slownika no "!"



