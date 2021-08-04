import random


class Student:

    def __init__(self,first_name,last_name):
        self.last_name = last_name
        self.first_name = first_name
        self.promote= False
        self._final_grades = []

    def add_final_grade(self, grade):
        self._final_grades.append(Grade(value=grade))
        if not grade.is_passing():
            self.promote = False

    def promote(self):
        self.promote = True


    # def print_self(self): zamienimy metode print_self na magiczna __str__
    #     print(f"student: {self.first_name} {self.last_name} prmoted:{self.promoted}")
    def __str__(self):
        return f"student: {self.first_name} {self.last_name} prmoted:{self.promote}"

    def __repr__(self):
        return f"<Student first_name='{self.first_name}',last_name= '{self.last_name}', promoted = {self.promote}>"



# class School :
#     MAX_STUDENTS_NUMBER = 20
#     def __init__(self,name,students):
#         self.name = name
#         self.students = students
#         self.promote_lucky_student()
#
#     def promote_lucky_student(self):
#         for index, student in enumerate(self.students):
#             if index % 3 == 0:
#                 student.promote()
#
#     def __str__(self):
#         students= ""
#         for student in self.students:
#             students += "\n"
#             students += str(student)
#         return f"School: {self.name},{len(self.students)},students: {students}"
#
#     def assign_student(self, student):
#         # if len(self.students) < School.MAX_STUDENTS_NUMBER:
#         if len(self.students) < self.MAX_STUDENTS_NUMBER:
#             self.students.append(student)
#         else:
#             print("Nie ma już miejsca!")
class School:

    MAX_STUDENTS_NUMBER = 20

    def __init__(self, name, students):
        self.name = name
        self.students = students
        self._promote_lucky_students()

    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def __str__(self):
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"School: {self.name}, with {len(self.students)} students: {students}"

    @classmethod
    def create_school_with_students(cls, school_name):
        number_of_students = random.randint(1, cls.MAX_STUDENTS_NUMBER)
        students = []
        for student_number in range(number_of_students):
            first_name = f"Student-{student_number}"
            last_name = "Smith"
            students.append(Student(first_name, last_name))

        school = School(school_name, students)
        return school

    def assign_student(self, student):
        # if len(self.students) < School.MAX_STUDENTS_NUMBER:
        if len(self.students) < self.MAX_STUDENTS_NUMBER:
            self.students.append(student)
        else:
            print("Nie ma już miejsca!")
# def __repr__(self):
    #     students_reps = []
    #     for student in self.students:
    #         students_reps.append(repr(student))
    #     all_students_repr = ", ".join(students_reps)

    # def promote(self,student):
    #     student.promote = True

        # return f"<School name='{self.name}',students=[{all_students_repr}]>"
    @classmethod
    def create_school_with_students(cls, school_name):
        number_of_students = random.randint(1,cls.MAX_STUDENTS_NUMBER)
        students = []
        for student_number in range (number_of_students):
            first_name = f"Student- {student_number}"
            last_name = "Smith"
            students.append(Student(first_name,last_name))
        school = School(school_name,students)
        return school


class Grade:
    FAILING_GRADE = 1

    def __init__(self,value):
        self.value = value
    def is_passing(self):
        return self.value > Grade.FAILING_GRADE


# def run_example():
#     school= create_school_with_students("Hogwart")
#     str_school = str(school)
#     print(str_school)
#     school_repr = repr(school)
#     print(school_repr)

    # print(school)  -  tak tez zadziała bez dwoch powyzszych linijek

class Money:
    def __init__(self,dollars, cents):
        self.dollars = dollars
        self.cents = cents
    def as_cents(self):
        return self.dollars * 100 + self.cents
    def __add__(self, other):
        all_cents = self.as_cents()+other.as_cents()
        dollars = int(all_cents /100)
        # all_cents % 100 to reszta z dzielenia przez 100
        cents = all_cents % 100
        return Money(dollars,cents)


    def __str__(self):
        return f"{self.dollars}$ and {self.cents} cents"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents()== other.as_cents()
    def __ne__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() != other.as_cents()
    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.as_cents() < other.as_cents()

def compare_money_list(first,second):
    for money in first:
        if money not in second:
            return False

    return True

def run_example():
    # print(f"{Money(dollars=1,cents=20)}=={Money(dollars=100,cents=2)}?")
    # print(Money(dollars=1,cents=20)==Money(dollars=100,cents=2))
    #
    # print(f"{Money(dollars=1, cents=20)}!={Money(dollars=100, cents=2)}?")
    # print(Money(dollars=1, cents=20) != Money(dollars=100, cents=2))
    #
    # print(f"{Money(dollars=1, cents=20)}<{Money(dollars=100, cents=2)}?")
    # print(Money(dollars=1, cents=20) < Money(dollars=100, cents=2))



    some_money=[
        Money(dollars=1, cents=20),
        Money(dollars=3, cents=50),
        Money(dollars=50, cents=20)

    ]


    other_money = [
        Money(dollars=50, cents=20),
        Money(dollars=3, cents=50),
        Money(dollars=1, cents=20),


    ]
    # print(compare_money_list(some_money,other_money))
    # school = create_school_with_students("Hogwart") od kiedy funkcja ta jest przeniesiona do wewnatrz klasy
    # jako metoda klasy, trzeba bedzie sie juz odwolac w inny sposob do niej
    school = School.create_school_with_students("Hogwart")
    print(school)

    print(f"w szkole może być maksymalnie {school.MAX_STUDENTS_NUMBER} uczniów")
#  co Ciekawe w ten sposob moge sie odwolywac juz do konkretnego elementu/zmiennej school. zamiast do calej
#  School. i ona tez bedzie miala dostep do tej wartosci zapisanej wewnatrz klasy

if __name__ =='__main__':
    run_example()