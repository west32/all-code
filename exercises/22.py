with open ("happynumbers.txt","r", encoding="utf-8") as happynumberfile:
    happynumbers= happynumberfile.read()

    print(happynumbers.replace("\n",","))


with open ("primenumbers.txt","r",encoding='utf-8') as primenumbersfile:
    primenumbers= primenumbersfile.read()
    print(primenumbers.replace("\n",","))

overlaping_numbers= []

for number in primenumbers.replace("\n",",").split(","):
    if number in happynumbers.replace("\n",",").split(",") and number not in overlaping_numbers:
        overlaping_numbers.append(int(number))

print(overlaping_numbers)