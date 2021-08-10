# Napisz funkcję która przyjmie dowolną liczbę argumentów
# pozycyjnych i zwróci napis powstały z połączenia ich z
# wykorzystaniem myślnika jako łącznika pomiędzy poszczególnymi argumentami.

def string(*args):
    result= ""
    for word in args:
        result += str(word)
        result += "-"
    return result[:-1]
def run_homework():

    result= string(1,4,"hello",3,5,"mama")
    print(result)

if __name__=="__main__":
    run_homework()



# LUB


def string(*args):

    return "-".join(args)

def run_homework():

    result= string("1","4","hello","3","5","mama")
    print(result)

if __name__=="__main__":
    run_homework()