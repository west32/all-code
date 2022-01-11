# Zadanie nr 1
# Poproś użytkownika o wprowadzenie ocen, które uzyskał/a.
#
# Wykorzystaj pętlę while, aby pytać o kolejne oceny i zakończyć wprowadzanie
# odpowiednim znakiem (np. X).
#
# Następnie, stosując pętlę for oblicz średnią z podanych ocen.

# grades = []
# grade_input= input("podaj ocene lub wcisnij 'x' aby zakończyć").lower()
#
# while grade_input != "x":
#     grade= int(grade_input)
#     grades.append(grade)
#     grade_input = input("podaj ocene lub wcisnij 'x' aby zakończyć").lower()
#
#
# grades_sum=0
# for grade in grades:
#     grades_sum += grade
# average = grades_sum/ len(grades)
#
# print (f"Twoja średnia wynosi {average:.2f} ")

# Zadanie nr 2
# Zmodyfikuj zadanie z poprzedniej lekcji dotyczące formatowania numeru telefonu.
#
# Zastąp pętlę while pętlą for (i enumerate).

# phone_number=input("podaj nr telefonu").replace("-","")
#
# modified_number=""
# for index, digit in enumerate(phone_number):
#     if index %3==0 and index != 0:
#         modified_number += "-"
#     modified_number += digit
#
# print(modified_number)

# Zadanie nr 3
# Wczytaj od użytkownika kolejne kategorie wydatków oraz dla każdej z nich dokonane wydatki.
#
# Zastosuj pętlę while, aby użytkownik mógł zakończyć wprowadzanie kategorii i wydatków.
#
# Stosując pętlę for oblicz procentowy udział każdego z wydatków w miesięcznym budżecie
# i wypisz wyniki oraz dodatkową informację, która powie o najbardziej znaczącej kategorii.

expenditures= {}

category=""

price=""

while category != "x":
    category = input("wprowadz kategorie wydatków, 'x' aby zakończyć ").lower()
    if category != "x":
        expenditures[category]={}
        expenditure = ""
        while expenditure != "x":
                expenditure = input(f"co kupiłeś z kategorii {category}? 'x' aby dodać kolejną kategorię ").lower()
                if expenditure != "x":
                    price= input(f"ile wydałeś na {expenditure}?")
                    expenditures[category][expenditure]=float(price)
                    print(expenditures)


all_cost=0
most_expensive_cat=None
bigest_udzial = 0
for  values  in expenditures.values():
    for expenditure in values.values():
        all_cost += expenditure

for categories, values in expenditures.items():
    for expenditure in values.values():

        udzial_kategorii= float(sum(values.values())/all_cost*100)
        print(f"Udział kategorii {categories} to {udzial_kategorii:.2f}%")
        if udzial_kategorii > bigest_udzial:
            bigest_udzial = udzial_kategorii
            most_expensive_cat = categories

for categories, dicts in expenditures.items():
    print(f"{categories}- {sum(dicts.values())}")

print(f"kategoria z największym udziałem to {most_expensive_cat} - {bigest_udzial:.2f}% wszystkich wydatków")


