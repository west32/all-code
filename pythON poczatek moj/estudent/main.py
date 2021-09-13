from estudent.errors import LogicError
from estudent.school import School
from estudent import data_generator
from estudent.department import BiochemDepartment,MathPhysicDepartment,Department
from  estudent.grade import Grade,FinalGrade
from estudent.student import Student
from estudent.subject import Subject
from estudent.grade_calculator import GradeCalculator
from estudent import data_generator
from estudent.school import School
from estudent import data_generator
import os



def run_example():
    students = data_generator.generate_students()

    students_data_file_path = os.path.join("data","students.txt")
    # with open (students_data_file_path,mode="w",encoding='utf-8') as students_file:
    #     for student in students:
    #         students_file.write(str(student))
    #         students_file.write(("\n"))

    new_students = data_generator.generate_students()
    with open(students_data_file_path, mode="a",encoding='utf-8') as student_file:
        for student in new_students:
            student_file.write(str(student))
            student_file.write("\n")





if __name__ == '__main__':
    run_example()


