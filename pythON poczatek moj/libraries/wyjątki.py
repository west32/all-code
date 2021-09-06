from estudent.grade_calculator import GradeCalculator
from estudent.student import Student


def run_example():
    student= Student(first_name="Bart", last_name="Juda")
    student = GradeCalculator.calculate_student_avg

if __name__ == "__main__":
    run_example()