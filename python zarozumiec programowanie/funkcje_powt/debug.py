def find_best_grade(grades_by_subject):
    best_grade=0
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade=best_grade_from_subject
    return best_grade

grades_data = {
    "historia": [5,5,4,5],
    "matma": [5,5,4,6],
    "fizyka": [3,4,2,5]
}

the_best_grade= find_best_grade(grades_data)
print(f"najlepsza ocena to {the_best_grade}")