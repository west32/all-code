lista = input("podaj liste zakupów oddzielając ją przecinkami")
lista=lista.split(',')

if len(lista) > 5:
    print("wg mnie lista jest całkiem długa")
else:
    print("wg mnie lista jest raczej krótka")
