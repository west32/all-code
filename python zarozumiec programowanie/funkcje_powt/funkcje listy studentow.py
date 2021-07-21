# Napisz funkcję, dodającą kolejne osoby do listy osób uczęszczających na zajęcia.
#
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem oraz
# listę już zapisanych osób, która domyślnie jest pusta.

list_friday = ["Kamil","Basia","Maciek"]
list_monday = []


def add_students(volunteers,list=None):
    if list is None:
        list = []
    volunteers= volunteers.split(",")
    # for person in volunteers:
    #     list.append(person)
    list += volunteers
    return list


list_volunteers = "Tomek,Zbyszek,Kasia,Ola"
print(add_students(list_volunteers, list_friday))
