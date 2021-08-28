# def find_best_grade(subjects_with_final_grades):
#     best_subject = None
#     best_final_grade = 0
#     # for subject,final_grade in subjects_with_final_grades.items():
#     #     if final_grade > best_final_grade:
#     #         best_final_grade = final_grade
#     #         best_subject= subject
#     # return best_subject,best_final_grade
#     for element in subjects_with_final_grades.items():
#         print("element type:",type(element))
#         subject = element[0]
#         final_grade = element[1]
#         if final_grade > best_final_grade:
#             best_final_grade = final_grade
#             best_subject = subject
# #         return best_subject,best_final_grade
#
# subject_with_final_grades = {
#     "Matematyka": 4,
#     "Historia" : 4,
#     "Fizyka" : 3,
#     "Biologia" : 5
# }
#
# best_subject, best_grade = find_best_grade(subject_with_final_grades)
# print(best_subject,best_grade)
# result = find_best_grade(subject_with_final_grades)
# print(result)
# print(type(result))

def run_avg_speed(name, distance, time):
    avg_speed = distance / time
    print(f"{name} biega z prędkością {avg_speed}")


run_data = ("Bob",20,2)
run_data(*run_data)