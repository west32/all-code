
# Napisz funkcję, która zapyta użytkownika o pierwsze trzy litery imienia.
#
# Jeżeli wprowadzone zostanie mniej lub więcej liter to powinna rzucić wyjątek.
#
# Wywołaj funkcję wewnątrz bloku try i skorzystaj z sekcji except, else oraz finally wypisując różne komunikaty.
class DigitsNumberError(Exception):
    pass


def first_three_digits():
    digits = input("podaj 3 pierwsze litery imienia: ")
    if len(digits) < 3:
        raise DigitsNumberError ("za mało")
    if len(digits) >3:
        raise DigitsNumberError ("za dużo")
    return digits

def run_homework():
    try:
        name = first_three_digits()
    except DigitsNumberError as error:
        print(f" nie prawidłowa liczba znaków: {error}")
    else:
        rest= input(" podaj pozostałe litery Twojego imienia")
    finally:
        print("Miło mi ja jestem Python :P")


if __name__=="__main__":
    run_homework()