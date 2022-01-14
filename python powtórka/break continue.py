import random
from random import sample, randint

# oceny = { "matematyka":0,
#           "fizyka":0,
#           "polski":0}
#
# for przedmiot in oceny:
#     ocena=int(input(f"podaj ocenę końcową z {przedmiot} "))
#     oceny[przedmiot]=ocena
#     if ocena ==1:
#         print ("kasę trzeba powtórzyć")
#         break
#     else:
#         print("gratulacje")
#
# print(oceny)


# 2
#
#
# expenditures= {}
#
# category=""
#
# price=""
#
# while True:
#     category = input("wprowadz kategorie wydatków, 'x' aby zakończyć ").lower()
#     if category == "x":
#         break
#
#         expenditures[category]={}
#         expenditure = ""
#         while True:
#                 expenditure = input(f"co kupiłeś z kategorii {category}? 'x' aby dodać kolejną kategorię ").lower()
#                 if expenditure == "x":
#                     break
#
#                 price= input(f"ile wydałeś na {expenditure}?")
#                 expenditures[category][expenditure]=float(price)
#                 print(expenditures)
#
#
# all_cost=0
# most_expensive_cat=None
# bigest_udzial = 0
# for  values  in expenditures.values():
#     for expenditure in values.values():
#         all_cost += expenditure
#
# for categories, values in expenditures.items():
#     for expenditure in values.values():
#
#         udzial_kategorii= float(sum(values.values())/all_cost*100)
#         print(f"Udział kategorii {categories} to {udzial_kategorii:.2f}%")
#         if udzial_kategorii > bigest_udzial:
#             bigest_udzial = udzial_kategorii
#             most_expensive_cat = categories
#
# for categories, dicts in expenditures.items():
#     print(f"{categories}- {sum(dicts.values())}")
#
# print(f"kategoria z największym udziałem to {most_expensive_cat} - {bigest_udzial:.2f}% wszystkich wydatków")


# 3

random_numbers = random.sample(range(100),random.randint(1,20))
print(random_numbers)

for number in random_numbers:
    if number %2==0:
        continue
    print(number)