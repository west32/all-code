# Zmodyfikuj zadanie drugie (dotyczące budżetu domowego) z lekcji dotyczącej break i continue (moduł 5).
#
# Zamknij spójne elementy programu w funkcje.


def pobierz_wydatki (category_name):
    category_values = []
    while True:
        category_value = (input(f"ile wydajesz na {category_name} ? 'x' aby zakonczyc  "))
        if category_value == 'x':
            return category_values
        float_wydatek= float(category_value)
        category_values.append(float_wydatek)

expanditures = {}
def pobierz_kategorie ():

    while True:
        category_name= input("na co wydajesz ? 'x' aby zakonczyc")
        if category_name == 'x':
            return expanditures

        print(expanditures)
        expanditures[category_name]=pobierz_wydatki(category_name)
        print(expanditures)

pobierz_kategorie()

#

#     category_name = input("na co wydajesz? aby zakonczyc 'x' ")
#     if category_name == 'x':
#         break
#     expanditures[category_name] = []
#     while True:
#         expanditure_value = input(f" ile wydajesz na {category_name}")
#         if expanditure_value == 'x':
#             break
#         expanditure_value = float(expanditure_value)
#         expanditures[category_name].append(expanditure_value)
# #

def oblicz_calkowite (expanditures):
    wynik = 0
    for category_values in expanditures.values():
        wynik +=sum(category_values)
    print(wynik)
    return wynik

oblicz_calkowite (expanditures)

def oblicz_procentowe (expanditures, calkowite_wyd):
    procentowe_wydat = {}
    for kategoria, wydatki in expanditures.items():
        calkowity_kategorii= sum(wydatki)
        calkowite_wyd= oblicz_calkowite(expanditures)
        procentowe_wydat[kategoria]= calkowity_kategorii *100 / calkowite_wyd
        print(f"{procentowe_wydat:.0f}")
        return procentowe_wydat
oblicz_procentowe(expanditures,calkowite_wyd=oblicz_calkowite(expanditures))





# calkowite_wydatki = 0
# for wydatki in expanditures.values():
#     calkowite_wydatki += sum(wydatki)
#     print (calkowite_wydatki)
# procentowe_wydatki = {}
# for categories,perc_exp in expanditures.items():
#     procentowe_wydatki[categories] = sum(perc_exp) *100 / calkowite_wydatki
# print(procentowe_wydatki)
#
# najwazniejsza_kat = None
# najwyzszy_proc = 0
# for kategoria, procent in procentowe_wydatki.items():
#     if procent > najwyzszy_proc:
#         najwyzszy_proc = procent
#         najwazniejsza_kat= kategoria
# print(f"najwiecej wydajesz na {najwazniejsza_kat} bo aż {najwyzszy_proc:.0f}% ")
