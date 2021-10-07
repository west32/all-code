# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


name = input("what's your name? ")
age= int(input ("How old are you ? "))
actual_year = 2021
number= int(input("give me a number "))

answear = (f" Hi {name}, you will 100 years old in {(100 - age) + actual_year }\n")
print(answear* number )
