def pole_prostokąta(a,b):
    pole= a * b
    return pole

def run_example():
    bok_a = int(input("podaj pole boku a "))
    bok_b = int(input("podaj pole boku b "))

    print(pole_prostokąta(bok_a,bok_b))

if __name__=="__main__":
    run_example()