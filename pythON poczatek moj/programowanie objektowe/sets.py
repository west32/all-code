import random

falvours = []
bob_flavourite_flavours = {"malinowy", "truskawkowy", "jagodowy"}
alice_favourite_flavours = {"pistacjowy", "truskawkowy", "orzechowy", "orzechowy", "orzechowy"}

# all_flavours= bob_flavourite_flavours.union(alice_favourite_flavours)
# print(bob_flavourite_flavours.issubset(all_flavours))

numbers = [random.randint(0,40) for _ in range (100)]
no_duplicates = set(numbers)
print(len(numbers))
print(len(no_duplicates))

digits = {number for number in range (10)}
print(f" czy udało sie wylosowac wszystkie liczbty? {digits.issubset(no_duplicates)}")
# print(bob_flavourite_flavours)
# print(alice_favourite_flavours)

# not_working_empty_set = {}
# empty_set = set()
#
# print(type(not_working_empty_set))
# print(type(empty_set))
#
# alice_favourite_flavours.add("waniliowy")
#
# alice_favourite_flavours.remove("pistacjowy")
# print(alice_favourite_flavours.pop())


# copy_of_flavours = alice_favourite_flavours.copy()
# alice_favourite_flavours.clear()

# print(alice_favourite_flavours)


