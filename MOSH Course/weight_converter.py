weight_input = int(input("What is your weight?"))
Lbs_or_Kg= input("(L)bs or (K)g?").upper()
if Lbs_or_Kg == "L":
    print(f" Your weight is {weight_input * 0.45} kg ")
elif Lbs_or_Kg =="K":
    print(f" Your weight is {weight_input / 0.45}")
else:
    print("There is only 2 options: (L) or (K)")