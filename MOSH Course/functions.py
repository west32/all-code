class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print (f"{self.name} talking to you")

john = Person(name="John Smith")
john.talk()