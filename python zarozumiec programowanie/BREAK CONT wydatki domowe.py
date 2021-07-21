# Zmodyfikuj rozwiązanie zadania trzeciego z lekcji dotyczącej pętli for (obliczanie wydatków domowych).
#
# Skorzystaj z instrukcji break, aby wyeliminować powtórzone wywołania funkcji input.


# moje rozwiazniae troche na okolo
expanditures = {}
# category_input = None
# while category_input !='x':
#     category_input = input("na co wydasz kase, aby przerwac wcisnij x ")
#     if category_input == 'x':
#         continue
#     expanditures[category_input] = []
#     expanditure_value_input = 0
#     while expanditure_value_input != 'x':
#         expanditure_value_input= input(f"ile chcesz wydac na {category_input}?  ")
#         if expanditure_value_input != 'x':
#             expanditure_value_input= float(expanditure_value_input)
#             expanditures[category_input].append(expanditure_value_input)
#         if expanditure_value_input =='x':
#             break
# rozwiazanie Mikolaja

while True:
    category_name = input("na co wydajesz? aby zakonczyc 'x' ")
    if category_name == 'x':
        break
    expanditures[category_name] = []
    while True:
        expanditure_value = input(f" ile wydajesz na {category_name}")
        if expanditure_value == 'x':
            break
        expanditure_value = float(expanditure_value)
        expanditures[category_name].append(expanditure_value)


print(expanditures)

calkowite_wydatki = 0
for wydatki in expanditures.values():
    calkowite_wydatki += sum(wydatki)
    print (calkowite_wydatki)
procentowe_wydatki = {}
for categories,perc_exp in expanditures.items():
    procentowe_wydatki[categories] = sum(perc_exp) *100 / calkowite_wydatki
print(procentowe_wydatki)

najwazniejsza_kat = None
najwyzszy_proc = 0
for kategoria, procent in procentowe_wydatki.items():
    if procent > najwyzszy_proc:
        najwyzszy_proc = procent
        najwazniejsza_kat= kategoria
print(f"najwiecej wydajesz na {najwazniejsza_kat} bo aż {najwyzszy_proc:.0f}% ")










