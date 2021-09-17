from estudent import data_generator
from estudent.persistance import load_students_from_csv,save_student_as_csv

def run_example():
    students = data_generator.generate_students(number_of_students=10)
    save_student_as_csv(students)
if __name__=="__main__":
    run_example()