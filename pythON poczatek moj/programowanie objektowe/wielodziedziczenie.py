class Grandpa:

    def say_hello(self):
        print("hello granny")

class Mother(Grandpa):
    def say_hello(self):
        print("hello mama")

class Father(Grandpa):
    def say_hello(self):
        print("hello father")

class Kido(Father,Mother):
    pass

    # def say_hello(self):
    #     print("hello kido")

def run_example():
    print(Kido.mro())

    # kid=Kido()
    # kid.say_hello()


if __name__=="__main__":
    run_example()