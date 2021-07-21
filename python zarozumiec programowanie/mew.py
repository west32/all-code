koniec = 'x'
odpowiedz = (input("wprowadz ocene, jesli to koniec wprowadz 'x'"))
oceny = []
while odpowiedz != koniec:
    oceny.append(float(odpowiedz))
    odpowiedz = (input("wprowadz ocene, jesli to koniec wprowadz 'x'"))
print(oceny)
sum_grades=0
for grade in oceny:
     sum_grades  += grade
print (f" Twoj średnia is {sum_grades/ len(oceny)}")



