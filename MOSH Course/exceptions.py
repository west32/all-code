try:
    age = int(input("Age:"))
    income = 20000
    risk = income /age
    print(age)
except ZeroDivisionError:
    print("zero can't be an age")
except ValueError:
    print("invalid value")