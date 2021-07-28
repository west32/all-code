class Student:
    def __init__(self,first_name,last_name):
        self.last_name = last_name
        self.first_name = first_name
        self.promoted = False
    def print_self(self):
        print(f"student: {self.first_name} {self.last_name} prmoted:{self.promoted}")
    def promote(self):
        self.promoted = True
def run_example():
   student = Student("Bartek", "Juda")
   student.promote()
   student.print_self()

if __name__ =='__main__':
    run_example()