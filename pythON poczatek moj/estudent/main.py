from estudent.school import School
from estudent import data_generator

def run_example():
   student = data_generator.generate_students()
   print((student.first_student))


if __name__ == '__main__':
    run_example()
