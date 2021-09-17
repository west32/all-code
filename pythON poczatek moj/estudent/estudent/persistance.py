import csv
from estudent.student import Student

# def load_students_from_csv(file_name="students.csv"):
#     with open(file_name,newline="") as student_file:
#         csv_reader = csv.reader(student_file)
#         students = []
#         for row_index,row in enumerate(csv_reader):
#             if row_index == 0:
#                 continue
#             grades_values = [int(value) for value in row[3].split(",")]
#             # student = Student(first_name=row[0], last_name=row[1])
#             # students.append(student)
#             # for grades_value in grades_values:
#             #     student.add_final_grade(grades_value)
#             # student.promoted = str_to_bool(row[2])
#
#             students.append(
#                 Student.from_csv(
#                     first_name=row[0],
#                     last_name=row[1],
#                     promoted=str_to_bool(row[2]),
#                     grades_values=grades_values
#                 )
#             )
#     return students




def str_to_bool(str_bool):
    if str_bool =="True":
        return True
    elif str_bool =="False":
        return False
    raise ValueError(f"{str_bool} to niepoprawna wartość dla typu bool")

def save_student_as_csv(students,file_name="students.csv"):
    with open (file_name,mode="w", newline="") as student_file:
        # csv_writer= csv.writer(student_file)
        csv_writer = csv.writer(student_file, delimiter=";", quotechar="|", quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["first_name", "last_name", "promoted", "final_grades"])
        for student in students:
            serialized_final_grades = ",".join([str(grade.value) for grade in student._final_grades])
            csv_writer.writerow([student.first_name, student.last_name, student.promoted,serialized_final_grades])

def load_students_from_csv(file_name="students.csv"):
    with open (file_name, newline="") as students_file:
        csv_reader = csv.reader(students_file)
        headers = next(csv_reader)
        return [
            Student.from_csv(
                first_name=row[0],
                last_name= row[1],
                promoted= str_to_bool(row[2]),
                grades_values=[int(value) for value in row[3].split(",")]
            )
            for row in csv_reader
        ]