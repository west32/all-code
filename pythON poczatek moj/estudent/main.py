from estudent.school import School
from estudent import data_generator
from estudent.department import BiochemDepartment,MathPhysicDepartment,Department
from  estudent.grade import Grade,FinalGrade
from estudent.subject import Subject



def run_example():

    best_grade = Grade (value=6)
    print (best_grade)
    print(best_grade.is_passing())

if __name__ == '__main__':
    run_example()


