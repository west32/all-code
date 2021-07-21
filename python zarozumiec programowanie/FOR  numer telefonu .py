# Poproś użytkownika o podanie numeru telefonu.
#
# Następnie wypisz informację ile razy występuje w nim każda cyfra.

# z zastosowaniem FOR

numer = input('podaj nr telefonu')
for index, digit in enumerate(numer):
    print(f"cyfra {numer[index]} występuje {numer.count(digit)} razy ")

#
# for digit in range (10):
#     digit_times_in_number = numer.count(str(digit))
#     print(f"cyfra {digit} występuje {digit_times_in_number} razy w Twoim numerze")