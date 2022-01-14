# phone_number=input("wpisz nr telefonu ")
#
#
# uniques_digits=""
# for digit in phone_number:
#     if digit not in uniques_digits:
#         uniques_digits +=digit
# for digit in uniques_digits:
#     print(f"{digit}-{phone_number.count(digit)}x")

capital= float(input("podaj kwote kredytu "))
percentage = float(input("ile % "))
time = int(input("na jak długo w latach? "))
initial_fees= float(input("jaka prowizja początkowa? "))

number_of_months= time*12
loan_month= capital / number_of_months
total_paid= initial_fees

for month_number in range(1,number_of_months +1):
    capital_to_be_paid = capital - (month_number -1)* loan_month
    installment = (capital_to_be_paid *percentage /100)/12 + loan_month
    total_paid+= installment
    print(f"Rata w miesiącu {month_number} wyniesie {installment:.2f}")

print(f"Zaciągając {capital} na tych warunkach spłacisz z odsetkami {total_paid}")
