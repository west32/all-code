# Stwórz funkcję, która przyjmuje jako argument zbiór liczb, losuje liczbę od 0 do 10 i zwraca otrzymany
# wcześniej zbiór powiększony o wylosowaną liczbę.
#
# Wywołuj funkcję tak długo aż w wynikowym zbiorze znajdą się wszystkie liczby od 0 do 10.
#
# Za każdym razem jako argument przekaż do niej zwrócony przez wcześniejsze wywołanie zbiór.
#
# Zaimplementuj dwa warianty tej funkcji - działający z argumentem typu set oraz takim typu
# frozenset (w tym przypadku niezbędne będzie skorzystanie z metody union).
#
# Zastanów się, czy da się jedną implementacją obsłużyć obydwa przypadki? A co w sytuacji, gdybyś
# chciała/chciał zapamiętać wszystkie “pośrednie” zbiory, żeby na końcu wypisać jak wyglądały kolejne próby?
import random


def func_set(numbers):
    number = random.randint (0,10)
    return numbers.add(number)
def func_frozenset (numbers):
    number = random.randint(0,10)
    return numbers.union({number})





def run_example():

    # numbers = set()
    numbers = frozenset()

    # frozenset_of_mine = frozenset()
    answear = None
    while  len(numbers) < 11:
        numbers = func_frozenset(numbers)
        print(numbers)

    print(numbers)
    #     # answear = input("zalosowac ponownie? t/n?")







    # flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
    # bob_favourite_flavours = frozenset(flavours)
    # print(type(bob_favourite_flavours))
    #
    # alice_favourite_flavours = frozenset({"Pistacjowy","Truskawkowy","Orzechowy", "Orzechowy"})
    #
    # common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
    # all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
    #
    #
    # set_of_set= {frozenset({"słony karmel","mango"}),frozenset({"Truskawkowy", " Śmietankowy"})}
    # print(set_of_set)
    #
    # # print(common_flavours)
    # print(all_flavours)




if __name__ == "__main__":
    run_example()