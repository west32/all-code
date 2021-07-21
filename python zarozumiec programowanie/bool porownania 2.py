lista = input("podaj liste zakupów oddzielając ją przecinkami")
lista=lista.split(',')
dlugosc_listy = len(lista)
lista_dluga = dlugosc_listy >= 10

print(f"Wg mnie lista jest długa\t\t{lista_dluga}")
