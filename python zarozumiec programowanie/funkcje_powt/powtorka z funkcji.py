# Napisz prosty symulator sklepu.
#
# W jednym pliku zdefiniuj dostępne produkty: nazwę (np. chleb i jabłka), dostępną ilość i cenę
# jednostkową. W innym zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości
# stworzy nowe zamówienie i doda je do listy zamówień. Zamówienie składa się z nazwy produktu, zamówionej
# ilości i łącznej ceny. Obydwa pliki umieść w pakiecie.
#
# Sklep uruchom poprzez plik main, w którym zaimportujesz funkcje do tworzenia zamówienia, wczytasz
# dane od użytkownika i wypiszesz łączny koszt zakupów. Zastosuj importowanie
# def put_brick():
#     print("-", "-", "-",sep="", end="" )
#
# def build_wall(wall_length):
#
#     for brick in range (wall_length):
#         put_brick()
#
# build_wall(3)

def calculate_investment_value (initial_value,percentage,years):
    # result = initial_value * (1 + percentage / 100) ** years
    # print(f" po {years} latach Twoja lokata bedzie wynosiła {result:.0f} złotych")
    return initial_value * (1 + percentage / 100) ** years

# initial_value= 10000
# percentage = 4
# years = 4
# calculate_investment_value(initial_value,percentage,years)


def ask_for_int(message):
    value=input(message)
    return int(value)

def run_calculator():
    print('witaj w kalulatorze lokaty!')
    initial_value = ask_for_int("jaki jest kapitał początkowy")
    percentage= ask_for_int("jaki procent")
    years= ask_for_int("ile lat")

    final_value= calculate_investment_value(initial_value,percentage,years)
    print(f" po {years} latach Twoja lokata bedzie wynosiła {final_value:.0f} złotych")


    long_term= years * 2

    alternative_value= calculate_investment_value(initial_value,percentage,long_term)
    print(f" po {long_term} latach, wartość Twojej lokaty bedzie wynosić {alternative_value:.0f} ")

option = None
while option != 'x':
    run_calculator()
    option = input("aby przerwac wcisnij 'x', aby kontynuować wcnisj inny dowolny klawisz ")