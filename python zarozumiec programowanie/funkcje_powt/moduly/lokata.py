import calculations.def_calculate_value

initial_value= float(input("jaki wkład własny? "))
percentage = int(input("jaki procent?"))
years = int(input("na ile lat? "))

value= calculations.def_calculate_value.calculate_value(initial_value,percentage,years)

print(f"Wartość Twojej lokaty po {years} latach bedzie wynosić {value:.0f}zł")