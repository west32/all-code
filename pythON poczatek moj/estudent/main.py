from estudent.school import School
from estudent import data_generator
from estudent.department import BiochemDepartment,MathPhysicDepartment,Department


def assign_students_to_department(department,students):
    not_qualified = []
    for student in students:
        if not department.assign_student(student):
            not_qualified.append(student)
    return not_qualified


def run_example():
    students_prefer_bio_chem = data_generator.generate_students(number_of_students=10)
    students_prefer_math_phys = data_generator.generate_students(number_of_students=10)
    students = data_generator.generate_students(number_of_students=5)

    bio_chem_department = BiochemDepartment(letter_identifier="A",year=1)
    math_phys_department = MathPhysicDepartment(letter_identifier="B", year=1)
    general_department = Department(letter_identifier="C",year=1)

    not_qualified_bio_chem = assign_students_to_department(bio_chem_department,students_prefer_bio_chem)
    not_qualified_match_phys = assign_students_to_department(math_phys_department,students_prefer_math_phys)
    not_qualified = assign_students_to_department(general_department,students)
    not_qualified += assign_students_to_department(general_department,not_qualified_bio_chem)
    not_qualified += assign_students_to_department(general_department, not_qualified_match_phys)

    print(bio_chem_department)
    print(math_phys_department)
    print(general_department)




if __name__ == '__main__':
    run_example()


