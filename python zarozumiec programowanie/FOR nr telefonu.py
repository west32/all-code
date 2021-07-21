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

# nr_telefonu = input('wprowadz nr telefonu')
# nr_telefonu= nr_telefonu.replace("-","")
# sformatowany_numer= ""
# for index, letter in enumerate(nr_telefonu):
#     if index %3 ==0 and index !=0:
#          sformatowany_numer += '-'
#     sformatowany_numer += letter
# print(sformatowany_numer)

nr_telefonu = input("wprowadz nr telefony")
nr_telefonu=nr_telefonu.replace("-", "")
sformatowany_nr = ""
index =0
for index, digits in enumerate(nr_telefonu):
    if index %3==0 and index != 0:
        sformatowany_nr += "-"
    sformatowany_nr += digits
print(sformatowany_nr)