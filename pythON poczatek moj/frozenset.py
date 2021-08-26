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


def func(set):
    number = random.randint (0,10)
    set.add(number)
    return set




def run_example():

    my_set = set()
    final_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    answear = None
    while answear != "n" or final_set == my_set:
        func(my_set)
        print(my_set)
        differences = final_set.difference(my_set)
        print(f"brakuje wciąż {differences}")
        answear = input("zalosowac ponownie? t/n?")







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