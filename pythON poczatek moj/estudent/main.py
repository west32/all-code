from estudent.school import School
from estudent import data_generator
from estudent.department import BiochemDepartment,MathPhysicDepartment,Department
from  estudent.grade import Grade,FinalGrade
from estudent.subject import Subject



def run_example():
    best_grade = Grade(value=6)
    failing_garde = Grade(value=1)
    print(best_grade)
    print(failing_garde)
    print(best_grade.is_passing())
    print(failing_garde.is_passing())

    # final_grade = FinalGrade(value=3)
    # print(final_grade)
    # print(final_grade.is_passing())

    math = Subject(identifier=1,name="Matematyka",is_obligatory=True)
    final_grade = FinalGrade(value=4,subject=math)
    print(final_grade)
if __name__ == '__main__':
    run_example()


