class Teacher:
    def __init__(self,name,subject):
        print("został wywołany konstruktor klasy bazowej")
        self.name = name
        self.subject = subject
        self.assign_departments= []

    def assign_department(self,department):
        self.assign_departments.append(department)

    def __str__(self):
        return f" Nauczyciel: {self.name} uczy: {self.subject} klasy: {self.assign_departments}"

class Tutor(Teacher):

    def __init__(self,name,subject,department):
        print("to ja konstruktor klasy potomnej ")
#         odwolanie do konstruktora klasy bazowej
        super().__init__(name,subject)
#         rozszerzenie klasy bazowej o dodatkowe pola
        self.guided_department = department

    # alternatywny sposob:
    # def __init__(self,department,*args,**kwargs):
    # super().__init__(*args,**kwargs)
    # self.guided_department = department

    def send_message_from_partents(self,message):
        print(f"Wiadomość od rodziców wysłana '{message}'")





def run_example():
    # teacher = Teacher(name="Bartek", subject="W-F")
    # teacher.assign_department("C1")

    tutor = Tutor(department="A2",name="Miszka", subject="unicornologia")
    print( tutor.guided_department)
    tutor.send_message_from_partents(message="Pozdrowienia")
    tutor.assign_department("A2")

    tutor.assign_department("B2")
    print(tutor.name)
    print(tutor.assign_departments)

if __name__=="__main__":
    run_example()