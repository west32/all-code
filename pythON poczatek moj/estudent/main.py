from estudent.school import School
from estudent import data_generator
from estudent.department import BiochemDepartment,MathPhysicDepartment,Department
from  estudent.grade import Grade,FinalGrade
from estudent.subject import Subject
from estudent.grade_calculator import GradeCalculator



def run_example():
   #
   # students = data_generator.generate_students(number_of_students=45)
   # school = School(name="Hogwart",students=[])
   # school.students = students

    student_avg = GradeCalculator.calculate_student_avg([])

if __name__ == '__main__':
    run_example()


