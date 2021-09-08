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





def run_example():
    student = Student (first_name="BOB",last_name="Bobowski")
    try:
        print(student.grades_avg)
    except LogicError as error:
        print(f"Błąd: {error}")





if __name__ == '__main__':
    run_example()


