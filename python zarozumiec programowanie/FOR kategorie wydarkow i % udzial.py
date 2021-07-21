# # Wczytaj od użytkownika kolejne kategorie wydatków oraz dla każdej z nich dokonane wydatki.
# #
# # Zastosuj pętlę while, aby użytkownik mógł zakończyć wprowadzanie kategorii i wydatków.
# #
# # Stosując pętlę for oblicz procentowy udział każdego z wydatków w miesięcznym budżecie i wypisz wyniki oraz dodatkową
# # informację, która powie o najbardziej znaczącej kategorii.

expenditures= {}
while True:
    category= input("na co wydajesz pięniądze, aby przerwać wcisnij 'x'")
    if category == 'x':
        break
    expenditures[category]=[]
    while True:
        category_expenditure= input(f"ile wydajesz na {category}, wcisnij 'x' aby dodac nową kategorie")
        if category_expenditure == 'x':
            break
        expenditures[category].append(int(category_expenditure))
        print(expenditures)
total_exp=0
for category, expenditure in expenditures.items():
    category_total_exp= sum(expenditure)
    total_exp += category_total_exp
    print(f"suma wydatków na {category} to {category_total_exp}zł")

percentage_expanditures= {}
for category, exp in expenditures.items():
    percentage_expanditures[category]= sum(exp)/total_exp *100

most_important_category= None
most_important_exp= 0
for category, exp in percentage_expanditures.items():
    if exp > most_important_exp:
        most_important_exp= exp
        most_important_category= category

print (f"na {most_important_category} wydajesz najwiecej bo aż {most_important_exp:.0f} %")








# expanditures = {}
# category_name = input(f" na co chcesz wydawac pieniądze, wcisnij 'x' aby przerwac ")
# while category_name != 'x':
#     expanditures[category_name] = []
#     value = (input(f" ile chcesz wydac na {category_name} ? aby przerwac wcisnij 'x' "))
#     expanditures[category_name].append(float(value))
#     while value !='x':
#         value = (input(f" ile chcesz wydac na {category_name} ? aby przerwac wcisnij 'x' "))
#         if value != 'x':
#             expanditures[category_name].append(float(value))
#             print(expanditures)
#
#     category_name = input(f" na co chcesz wydawac pieniądze, wcisnij 'x' aby przerwac " )
#
# print(expanditures)
#
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
# print(f"najwiecej wydajesz na {kategoria} bo aż {najwyzszy_proc:.0f}% ")










