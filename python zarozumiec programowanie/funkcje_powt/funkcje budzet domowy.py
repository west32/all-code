# Zmodyfikuj zadanie drugie (dotyczące budżetu domowego) z lekcji dotyczącej break i continue (moduł 5).
#
# Zamknij spójne elementy programu w funkcje.

def load_expenditures(category_name):
    expenditures_values= []
    while True:
        expenditure= input(f"ile chcesz przeznaczyc na {category_name}, aby wprowadzic nowa kategorie wisnij 'x' ")
        if expenditure =='x':
            return expenditures_values
        expenditure_value=float(expenditure)
        expenditures_values.append(expenditure_value)
def load_expenditures_by_categories ():
    expenditures= {}
    while True:
        category_name= input("na co chcesz wydawać pieniądze' aby zakonczyć wcisnij 'x'")
        if category_name=='x':
            return expenditures
        expenditures[category_name]=load_expenditures(category_name)

def calculate_total_exp(expenditures):
    result= 0
    for category_exp in expenditures.values():
        result += sum(category_exp)
    return result

def calculate_expenditures_percentage(expenditures,total_exp):
    percentage_by_category_name= {}
    for category_name,category_expenditures in expenditures.items():
        total_category_expenditures = sum(category_expenditures)
        percentage_by_category_name[category_name]=total_category_expenditures/total_exp*100
    return percentage_by_category_name
def find_most_important_category(percentage_by_category_name):
    highest_percentage_category=None
    highest_percentage= 0
    for category,percentage in percentage_by_category_name.items():
        if percentage > highest_percentage:
            highest_percentage=percentage
            highest_percentage_category=category
    return highest_percentage_category,highest_percentage

def print_the_most_imp_category(category_name,percentage):
    print(f"najwięcej wydajesz na {category_name} bo aż {percentage:.0f}%")

def print_category_info(category,percentage):
    print(f"na {category} wydajesz {percentage:.0f}%")

expenditures_by_categories=load_expenditures_by_categories()
total_expenditures=calculate_total_exp(expenditures_by_categories)
expenditures_percentage=calculate_expenditures_percentage(expenditures_by_categories,total_expenditures)
most_important_category, most_important_category_percentage=find_most_important_category(expenditures_percentage)

if most_important_category is not None:
    print_the_most_imp_category(most_important_category, most_important_category_percentage)

for category,percentage in expenditures_percentage.items():
    print_category_info(category,percentage)