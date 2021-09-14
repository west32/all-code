import csv
from estudent.student import Student

def load_students_from_csv(file_name="students.csv"):
    with open(file_name,newline="") as student_file:
        csv_reader = csv.reader(student_file)
        students = []
        for row_index,row in enumerate(csv_reader):
            if row_index == 0:
                continue
            grades_values = [int(value) for value in row[3].split(",")]
            student = Student(first_name=row[0], last_name=row[1])
            students.append(student)
            for grades_value in grades_values:
                student.add_final_grade(grades_value)
            student.promoted = str_to_bool(row[2])

            # students.append(
            #     Student.from_csv(
            #         first_name=row[0],
            #         last_name=row[1],
            #         promoted= str_to_bool(row[2]),
            #         grades_values=grades_values)
            # )
    return students



def str_to_bool(str_bool):
    if str_bool =="True":
        return True
    elif str_bool =="False":
        return False
    raise ValueError(f"{str_bool} to niepoprawna wartość dla typu bool")