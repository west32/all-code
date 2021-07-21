# lista_dan =input('wymien dania oddzielajac je przecinkiem')
# lista_dan.split(",")
# lista_index = 0
# while lista_index < len(lista_dan):
#     print(f"[{lista_index + 1}]miejsce zajmuje na liscie -> {lista_dan[lista_index]}")
#     lista_index += 1
#
lista_dan = input('wpisz swój liste dan z przecinkami: ')
lista_dan = lista_dan.split(",")
print(lista_dan)
lista_index = 0
while lista_index< len(lista_dan):
    print(f"{lista_index +1 } miejsce na Twojej liscie dań to -> {lista_dan[lista_index]}")
    lista_index += 1

