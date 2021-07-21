# Napisz funkcję, dodającą kolejne osoby do listy osób uczęszczających na zajęcia.
#
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem oraz listę już zapisanych osób, która domyślnie jest pusta.

def dodaj_osoby(osoby_str,lista=None):
    if lista is None:
        lista = []
    osoby_str= input('wprowadz osoby i oddziel przecinkiem')
    imiona=osoby_str.split(',')
    for imie in imiona:
        lista.append(imie)
    # lista +=
    # print(lista)
    return lista

oczekujący2= ""
oczekujacy= ""
lista_globalna= dodaj_osoby(oczekujacy)
print(f"lista globalna-{lista_globalna}")
lista_globalna= dodaj_osoby(oczekujący2,lista=lista_globalna)
print(f"lista globalna- {lista_globalna}")
kurs_piatkowy=dodaj_osoby(oczekujacy)
print(f"kurs piątkowy- {kurs_piatkowy}")







# def add_people_to_classes(names_str, participants=None):
#     if participants is None:
#         participants = []
#     names = names_str.split(',')
#     for name in names:
#         participants.append(name)
#     # participants += names
#     return participants
#
# attendees_names = "Ola,Bob,Ala,Kuba"
# monday_course_participants = add_people_to_classes(attendees_names)
# print(monday_course_participants)
# attendees_names = "PaweĹ,Dominika"
# monday_course_participants = add_people_to_classes(attendees_names, participants=monday_course_participants)
# print(monday_course_participants)
#
#
# attendees_names = "Ania,Krzysztof"
# friday_course_participants = add_people_to_classes(attendees_names)
# print(friday_course_participants)