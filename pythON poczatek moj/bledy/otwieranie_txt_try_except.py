path_to_file= "plain_text.txt"


try:
    plain_text_file = open(path_to_file, mode="r")
    try:
        print("Wczytaj dane")
        text_data = plain_text_file.read()
    finally:
        print("zamykamy plik")
        plain_text_file.close()
except IOError:
    print("Nie udało sie wczytać danych...")
else:
    print("Dane z pliku:")
    print(text_data)
print("Do zobaczenia później")