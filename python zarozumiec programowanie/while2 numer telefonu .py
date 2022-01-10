# numer = input('podaj numer telefonu')
# numer = numer.replace("-", "")
# numer_index = 0
# sformatowany_numer = ""
# while numer_index < len(numer):
#     sformatowany_numer +=numer[numer_index]
#     numer_index += 1
#     if numer_index %3==0:
#         sformatowany_numer +="-"
# print (sformatowany_numer)

numer = input('podaj numer telefonu')
numer = numer.replace("-", "")
sformatowany_numer = ""
for index, letter in enumerate(numer):
    if index % 3 == 0 and index != 0:
        sformatowany_numer += "-"
    sformatowany_numer += letter
print(sformatowany_numer)
