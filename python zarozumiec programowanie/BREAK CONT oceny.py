# przedmioty = {
#     "polski" : "",
#     "matma" : "",
#     "biologia" : "",
#     "geografia" : "",
#     "wf" : "" ,
# }
#
# for przedmiot, ocena in przedmioty.items():
#     ocena_input=input(f" jaką ocene masz z {przedmiot}")
#     if ocena_input == "1":
#         print("sashea away")
#         break
#     przedmioty[przedmiot] = ocena_input
# else:
#     print(f"condragulation Twoje oceny to \n {przedmioty}")

# lub

przedmioty = ['polak', 'matma', 'historia','wf']
oceny = []

for przedmiot in przedmioty:
    ocena= int(input(f"co dastałes z {przedmiot}? "))
    if ocena == 1:
        print('sashay away')
        break
    else:
        oceny.append(ocena)
else:
    print(f"condrugulation zdales z ocenami {oceny}")