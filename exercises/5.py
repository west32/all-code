# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("give me a number: "))
if number %2==0:
    print("this is an even number ")
elif number %4== 0:
    print ("different message ")
else:
    print ("this is an odd number ")

num= int(input("give me a first number: "))
check = int(input("gimme anoter one: "))
if num %check==0 :
    print(f" {check} divides evenly into {num} ")
else:
    print("different appropriate message")