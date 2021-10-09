# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

def get_number():
    number= input("Enter number: ")
    if number == "exit":
        return number
    else:
        return int(number)
def get_divisors (number):

    divisors = []
    for num in range (1,number):
        if number % num == 0:
            divisors.append(num)
    return divisors


number = 0
while number != "exit":
    number= get_number()
    if number =="exit":
        break
    divisors = get_divisors(number)
    if len(divisors)> 1:
        print("this number it's not a prime number")
    else:
        print("this is prime number ")