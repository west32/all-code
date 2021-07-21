# Zapytaj użytkownika ile miesięcznie wydaje pieniędzy na:
#
# jedzenie
# rozrywkę
# opłaty
# inne
# Oblicz udział procentowy każdej kategorii w łącznych wydatkach.
#
# Następnie poproś użytkownika o wybór kategorii i wypisz jaki jest jej udział procentowy.
food = float(input('ile na jedzenie'))
fun = float(input('na dziwki'))
bils = float(input('na czynsz?'))
others = float(input('na inne?'))

razem= food + fun +bils +others

kategorie = {
    "jedzenie": food *100 / razem,
    "dziwki": fun * 100 / razem,
    "bils": bils * 100 / razem,
    "others": others * 100 / razem
}


wybrana = (input("wybierz kategorie sposród jedzenie/dziwki/bils/othets"))
print(f"na {wybrana} wydajesz {kategorie[wybrana]:.0f}%")