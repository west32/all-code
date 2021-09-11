path_to_file="plain_text.txt"
#
# try:
#     with open(path_to_file, mode="r") as plani_text_file:
#         text_data = plani_text_file.read()
# except IOError:
#     print("Nie udało sie wczytać danych...")
# else:
#     print("Dane z pliku:")
#     print(text_data)
#
# print ("Do zobaczenia")

# lub

def proces_text():
    with open("plain_text.txt",mode="r") as plain_txt:
        text_data = plain_txt.read()

    print("Dane z pliku:")
    print(text_data)

def run_example():
    try:
        proces_text()
    except IOError:
        print("Cos poszło nietak...nie udało sie wczytać danych")

    print("do zobaczenia ")

run_example()