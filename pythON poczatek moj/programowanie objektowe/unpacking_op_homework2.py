# Zadanie nr 2
# Napisz funkcję, która przyjmie dowolną liczbę argumentów nazwanych
# i wypisze sposób w jaki została wywołana, tzn.
# poszczególne nazwy argumentów, znak równa się i wartość (np. first_name=Mikołaj, age=134).

def print_function (**kwargs):

    call_str=""
    for key,value in kwargs.items():
        call_str += f"{key} = {value},"
    print(call_str)

def run_homework():
    print_function(imie="Baretek", nazwisko="Juda", partenr="Miszka")

if __name__=="__main__":
    run_homework()