from estudent import data_generator
from estudent.school import School


def run_example():
    students = data_generator.generate_students(number_of_students=250)
    school = School(name="Mała szkoła",students=[])
    school.students = students

    
if __name__ == "__main__":
    run_example()