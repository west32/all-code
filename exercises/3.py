# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class GetPrintString:
    def __init__(self):
        self.str=""


    def get_string(self):
        self.str = input("write something")
        return self.str

    def print_string(self,):
        print(self.str.upper)

object = GetPrintString
object.get_string
