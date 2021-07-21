# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
#
# Następnie, przeanalizuj je i wypisz informację czy zdał/zdała do kolejnej klasy.
#
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki albo jeżeli ma się jedną jedynkę,
# ale średnia ze wszystkich ocen jest wyższa niż 3.5.
lista_pal = []
matematyka = int(input("jaką masz ocene z majcy?"))
if matematyka ==1:
    lista_pal.append('matematyka')
polski = int(input("jaką ocene masz z polaka?"))
if polski == 1:
    lista_pal.append("polski")
biologia = int(input("jaką ocene masz z bioli?"))
if biologia ==1:
    lista_pal.append("biologia")
geografia = int(input("jaką ocene masz z gegry "))
if geografia ==1:
    lista_pal.append("geografia")
wf = int(input("jaką ocene masz wuefu?"))
if wf == 1:
    lista_pal.append("wf")


srednia = float((matematyka + polski + biologia + geografia + wf)/5)
1
if len(lista_pal) <1:
         print(f"zdałeś a Twoja średnia wynosi {srednia}")
else:
    if len(lista_pal)==1:
        if srednia >3.5:
            print(f"zdałeś a Twoja srednia wynosi {srednia} ")
        else:
            print(f"nie zdałeś z powodu zbyt niskiej sredniej: {srednia} przy jedynce z {lista_pal}")
    if len(lista_pal) > 1:
        print(f"nie zdałeś z powodu pał z {lista_pal}")