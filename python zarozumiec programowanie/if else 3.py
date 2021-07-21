# Pobierz te same informacje na temat miesięcznych wydatków w różnych kategoriach.
#
# Wypisz jednak informacje na temat procentowego udziału najbardziej znaczącej kategorii.


# food = float(input('ile na jedzenie'))
# fun = float(input('na dziwki'))
# bils = float(input('na czynsz?'))
# others = float(input('na inne?'))
#
# razem= food + fun +bils +others
#
# kategorie = {
#     "jedzenie": food *100 / razem,
#     "dziwki": fun * 100 / razem,
#     "bils": bils * 100 / razem,
#     "others": others * 100 / razem
# }
#
# if food > bils:
#     if food > fun:
#         if food > others:
#              print(f"na jedzenie wydajesz najwięcej bo aż {kategorie['jedzenie']:.0f}%")
# if fun > food:
#     if fun > bils:
#         if fun > others:
#             print(f"na dziwki wydajesz najwięcej bo aż {kategorie['dziwki']:.0f}%")
# if bils > food:
#     if bils > fun:
#         if bils > others:
#             print(f"na rachunki wydajesz najwięcej bo aż {kategorie['bils']:.0f}%")
# if others > food:
#     if others > fun:
#         if others > bils:
#             print(f"na inne wydajesz najwięcej bo aż {kategorie['inne']:.0f}%")

# lub

most_important_category = "jedzenie"

if expenditures_percentage["rozrywka"] > expenditures_percentage[most_important_category]:
    most_important_category = "rozrywka"

if expenditures_percentage["opłaty"] > expenditures_percentage[most_important_category]:
    most_important_category = "opłaty"

if expenditures_percentage["inne"] > expenditures_percentage[most_important_category]:
    most_important_category = "inne"

print(f"Najwiecj wydajesz na {most_important_category} - {expenditures_percentage[most_important_category]:.0f}% wszystkich wydatkĂłw")