# metoda join stosuje poday string jako łącznik do scalenia listy napisów w jeden
# account_number_parts=["1234","4567", "5678", "6789"]
# print("-".join(account_number_parts))
# # pusty napis tez moze byc łącznikiem
# print("".join(account_number_parts))

# metody lstrip,rstrip oraz strip usuwaja znaki z lewej,prawej i obu stron napisu
# domyslnie usuwa odstepy
# ale jak przekazemy znaki ktore ma usunac to tez je usunie
# name = " -| Bartłomiej |- "
# left_clear = name.lstrip("-| ")
# right_clear = name.rstrip("-| ")
# both_clear = name.strip("-| ")
# print(f"{left_clear} Juda")
# print(f"{right_clear} Juda")
# print(f"{both_clear} Juda")

# Metody startswith oraz endswith sprawdzaja czy napis odpowierdnio zaczyna sie i konczy prefixem/ sufixem
# opcjonalne argumenty pozwalaja podac inny niz poczatek/koniec napisu zakres wyszukiwania

# last_name= "Juda"

# print(last_name.startswith("Ju"))
# print(last_name.startswith("da"))
# print(last_name.endswith("da"))
# print(last_name.endswith("Ju"))

# metoda zfill "dopełnia" napis zerami do osiagniecia podanej długosci.
# jest to przydatne np do budowania identryfikatorow o okreslonym formacie
# number = 135
# identifier = str(number).zfill(8)
# print(identifier)

# metody find oraz index pozwalaja pierwszy index pod ktorym wystepuje ciag znakow w napisie
# sentence= "ale dzisiaj ładny dzień! Wczoraj też był dobry dzień"
# print (sentence.find("dzień"))
# print(sentence.index("dzień"))

# opcjonalne argumenty pozwalają podać inny zakres wyszukiwania
# (wyszukiwanie w części napisu [start:end] - domyslnie od poczatku do końca
# print(sentence.find("dzień",20))
# print(sentence.index("dzień",24))

# Index działa tak samo jak find, przy czym jeżeli ciąg  znaków nie zostanie znaleziony
# find zwraca -1 a index rzuca błąd
# print(sentence.find("tego tam nie ma "))
# print(sentence.index("tego tam nie ma "))

# fstringi zostaly wprowadzone w pythonie 3.6
import random

language = "Python"
python_age = 30
# message = f"{language} ma juz prawie {python_age} lat"
# print(message)

# wczesniejszym sposobem na formatowanie napisow jest tzw. New style formatting,czyli metoda format na str
# wystepuje ona w kilku wariantach - po pierwsze puste nawiasy i uzupelnianie wg kolejnosci
# message= "{} ma juz praiwe {} lat".format(language,python_age)
# print(message)

# 2
# message = "{0} ma juz prawie {1} lat".format(language,python_age)
# print(message)

# 3

# message ="{language} ma juz prawie {age} lat".format(language=language,age=python_age)


# 4
# message= "%(language)s ma juz prawie %(age)d lat" %{"language": language, "age": python_age}


# 5

# message = "%s ma juz prawie %d lat" % (language,python_age)
# print(message)

# Zadanie nr 1
# Napisz funkcję, która wczyta od użytkownika jej/jego imię i nazwisko,
# “wyczyści je” z białych znaków na początku i końcu tekstu, a następnie
# wypisze jakieś zdanie z tymi danymi np. “Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)”

# def nice_to_meet_you():
#     first_name = input("Jak masz na imie? ")
#     first_name_strip= first_name.strip()
#     last_name = input("Jakie jest Twoje nazwisko? ")
#     last_name_strip = last_name.strip()
#     print(f"Nazywasz sie {first_name_strip} {last_name_strip} - jak miło Cie poznac :) ")
#
# nice_to_meet_you()

# Zadanie nr 2
# Napisz funkcję generującą losowy identyfikator. Identyfikator powinien być w formacie 00001, tzn.
# zawsze o długości pięciu znaków, dopełniony z lewej strony odpowiednią liczbą zer.

# def generate_identifier():
#     number = random.randint(1,9999)
#     identifier = str(number).zfill(5)
#     return identifier
#
# identifier = generate_identifier()
# print(identifier)

# Zadanie nr 3
# Wczytaj od użytkownika jej/jego ulubione kolory (jako jeden napis, np. rozdzielony przecinkiem).
#
# Sprawdź, czy znajduje się wśród nich niebieski, a następnie wypisz odpowiedni komunikat.

# favourite_color = input("jakie są twoje ulubione kolory? wypisz oddzielając je przecinkiem " )

# if favourite_color.lower().find("niebieski") > -1:
#     print("wśród Twoich ulubionych kolorów jest niebieski")
# else:
#     print("niebieski nie jest Twoim ulubionym kolorem")

# Zadanie nr 4
# Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać metodę format.

# def nice_to_meet_you():
#     first_name = input("Jak masz na imie? ")
#     first_name_strip= first_name.strip()
#     last_name = input("Jakie jest Twoje nazwisko? ")
#     last_name_strip = last_name.strip()
#     print("Nazywasz sie {} {} - jak miło Cie poznac :) ".format(first_name_strip,last_name_strip))
#
# nice_to_meet_you()

# Zadanie nr 5
# Zmodyfikuj rozwiązanie zadania pierwszego, tak aby do wypisywania wykorzystać formatowanie z procentem.

def nice_to_meet_you():
    first_name = input("Jak masz na imie? ")
    first_name_strip= first_name.strip()
    last_name = input("Jakie jest Twoje nazwisko? ")
    last_name_strip = last_name.strip()
    print("Nazywasz sie %s %s - jak miło Cie poznać :) " % (first_name_strip,last_name_strip))
#
nice_to_meet_you()