from estudent.school import School
from estudent import data_generator
from estudent.department import BiochemDepartment,MathPhysicDepartment,Department
from  estudent.grade import Grade,FinalGrade
from estudent.subject import Subject
from estudent.grade_calculator import GradeCalculator



def run_example():
    from estudent import data_generator
    from estudent.school import School

    def run_example():
        students = data_generator.generate_students(number_of_students=45)
        school = School(name="Mała szkoła", students=[])
        school.students = students

    if __name__ == "__main__":
        run_example()

if __name__ == '__main__':
    run_example()


