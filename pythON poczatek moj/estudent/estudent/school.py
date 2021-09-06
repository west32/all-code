import random

from estudent.config import Config
from estudent.student import Student


class School:
    MAX_STUDENTS_PER_DEPARTMENT = 1
    MAX_STUDENTS_NUMBER = 50

    def __init__(self, name, students):
        self.name = name
        self._students = students
        self._promote_lucky_students()
        self.depatments = self._split_students_to_departments()

    def _promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()

    def _split_students_to_departments(self):
        departments = {}
        departments_letters = ["A","B","C","D","E","F"]
        places_in_departments = len(departments_letters) * School.MAX_STUDENTS_PER_DEPARTMENT
        if places_in_departments < len(self._students):
            raise Exception("Nie wystarczająca liczba miejsc w klasach!")

        current_department_number = -1
        for index, student in enumerate(self.students):
            if index % School.MAX_STUDENTS_PER_DEPARTMENT == 0:
                current_department_number +=1

            current_department = departments_letters[current_department_number]
            if current_department not in departments:
                departments[current_department] = []

            departments[current_department].append(student)
        return departments

    def __str__(self):
        # students = ""
        # for student in self.students:
        #     students += "\n"
        #     students += str(student)
        result= ""
        for department_name, students_in_department in self.depatments.items():
            result += f"oddział {department_name} \n"
            for student in students_in_department:
                result += f"{student}\n"

        return f"Szkoła: {self.name}, z {len(self.students)} uczniami: \n {result}"




    @property
    def best_student(self):
        if len(self.students):
            return sorted(self.students, key=lambda  student: student.grades_avg, reverse=True)[0]
        return None

    # def assign_student(self, student):
    #     if len(self.students) < School.MAX_STUDENTS_NUMBER:
    #         self._students.append(student)
    #     else:
    #         print("Nie ma już miejsca!")

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self,value):
        if len(value) < School.MAX_STUDENTS_NUMBER:
            self._students = value

        else:
            raise Exception(
                f"W szkole jest tylko {School.MAX_STUDENTS_NUMBER} miejsc, nie można przypisać {len(value)} uczniów"
            )
        self.depatments = self._split_students_to_departments()