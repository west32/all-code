numbers = [3,34,53,2,64,234,643,23,54,6,23,54,]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)