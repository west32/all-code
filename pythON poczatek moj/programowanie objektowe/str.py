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
sentence= "ale dzisiaj ładny dzień! Wczoraj też był dobry dzień"
# print (sentence.find("dzień"))
# print(sentence.index("dzień"))

# opcjonalne argumenty pozwalają podać inny zakres wyszukiwania
# (wyszukiwanie w części napisu [start:end] - domyslnie od poczatku do końca
# print(sentence.find("dzień",20))
# print(sentence.index("dzień",24))

# Index działa tak samo jak find, przy czym jeżeli ciąg  znaków nie zostanie znaleziony
# find zwraca -1 a index rzuca błąd
print(sentence.find("tego tam nie ma "))
print(sentence.index("tego tam nie ma "))