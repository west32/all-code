# import os
#
# def process_text_file(file_path):
#     with open(file_path,mode="r") as my_txt_file:
#         text_data = my_txt_file.read()
#     print("Dane z pliku")
#     print(text_data)
#
# def run_example():
#     # local_path= "my_txt.txt"
#     # path_in_dir = "some_directory\\another_file.txt"
#     path_in_dir = os.path.join("some_directory", "another_file.txt")
#     try:
#         process_text_file(path_in_dir)
#     except IOError:
#         print("Nie udało sie wczytać danych")
#     print("Do zobaczenia ")
#
# if __name__=="__main__":
#     run_example()

with open ("plain_text.txt", mode="r") as plain_text_file:
    for line_number,line in enumerate(plain_text_file):
        print(f"{line_number}) {line}")
#
# Rozbuduj rozwiązanie zadania trzeciego z lekcji 167. PP: Wyjątki w Pythonie o utrwalanie złożonych zamówień.
#
# Przed wyłączeniem programu dopisz złożone zamówienie (wynik wykonania str na obiekcie zamówienia) do pliku orders.txt.
#
# Plik orders.txt powinien znajdować się w katalogu data - wykorzystaj ścieżkę względną by się do niego odwołać.