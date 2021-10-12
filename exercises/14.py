# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity
# to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate





def fibonnaci_numbers():
    number = int(input("how many Fibonnacci numbers you want me to generate? "))
    numbers=[]
    if number == 1:
        numbers = [1]
    elif number == 2:
        numbers=[1,1]
    elif number > 2:
        numbers=[1,1]
        while len(numbers) != number:
            new_number= numbers[-1] + numbers [-2]
            numbers.append(new_number)
    return numbers

print(fibonnaci_numbers())