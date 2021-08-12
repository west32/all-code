from estudent.school import School
from estudent import data_generator

def run_example():
    students = data_generator.generate_students()
    school = School(name="Hogwart", students= students)
    # best_student = school.best_student
    # print(school)

    new_student = data_generator.generate_students(number_of_students=8)
    school.students= new_student
    print(school)

    # too_many_students = data_generator.generate_students(number_of_students=100)
    # school.students = too_many_students
    # print(school)

    # print(f"średnia ocen najlepszego ucznia {best_student.grades_avg}")



if __name__ == '__main__':
    run_example()
