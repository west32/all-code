#
# odpowiedz = (input("wprowadz ocene, jesli to koniec wprowadz 'x'"))
# oceny = []
# while odpowiedz != 'x':
#     oceny.append(float(odpowiedz))
#     odpowiedz = (input("wprowadz ocene, jesli to koniec wprowadz 'x'"))
#
# srednia = sum(oceny) / len(oceny)
# print(srednia)
#
#
odpowiedz = (input('wprowdz ocene:'))
oceny= []
while odpowiedz != 'x':
    oceny.append(float(odpowiedz))
    odpowiedz = (input("wprowadz ocene, jesli to koniec wcisnij 'x'"))
suma_ocen =0
for suma in oceny:
    suma_ocen += suma

print (f" Twoja srednia po uzyskaniu ocen: {oceny} to: {suma_ocen / len(oceny):.2f}")