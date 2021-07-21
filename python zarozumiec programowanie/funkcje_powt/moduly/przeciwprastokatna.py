# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na
# podstawie otrzymanych długości przyprostokątnych.
#
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
#
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:
#
# sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
# pow(x, y) - podnosi x do potęgi y
import math
def calculate_c(a,b):
    return math.sqrt(pow(a,2)+pow(b,2))

a = int(input('ile wynosi bok a? '))
b = int(input('ile wynosi bok b?'))
c= calculate_c(a,b)
print(f"c= {c}")