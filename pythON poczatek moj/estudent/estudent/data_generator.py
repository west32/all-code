import random
from estudent.student import Student
from estudent.school import School
from estudent.config import Config
from estudent.StudentList import StudentList

def generate_students(number_of_students = None):
    if number_of_students is None:
         number_of_students = random.randint(1, School.MAX_STUDENTS_NUMBER)


    students = StudentList()
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        student = Student(first_name, last_name)
        students.append(student)
        for _ in range(Config.RANDOM_FINAL_GRADES_NUMBER):
            final_grade = random.randint(Config.MIN_RANDOM_GRADE, Config.MAX_RANDOM_GRADE)
            student.add_final_grade(final_grade)
    return students