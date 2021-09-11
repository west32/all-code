import os

def process_text_file(file_path):
    with open(file_path,mode="r") as my_txt_file:
        text_data = my_txt_file.read()
    print("Dane z pliku")
    print(text_data)

def run_example():
    # local_path= "my_txt.txt"
    # path_in_dir = "some_directory\\another_file.txt"
    path_in_dir = os.path.join("some_directory", "another_file.txt")
    try:
        process_text_file(path_in_dir)
    except IOError:
        print("Nie udało sie wczytać danych")
    print("Do zobaczenia ")

if __name__=="__main__":
    run_example()