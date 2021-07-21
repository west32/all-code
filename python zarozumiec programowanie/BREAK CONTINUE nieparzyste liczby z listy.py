lista = []
while len(lista) < 10:
    lista_input =(input('wporwawdz liczby do listy aby zakonczyc wcisnij x '))
    if lista_input == 'x':
        break
    lista_input = int(lista_input)
    lista.append(lista_input)

    print(lista)

for liczba in lista:
    if liczba %2 ==0:
        continue
    print( liczba)