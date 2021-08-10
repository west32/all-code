# def calculate_sum_via_list(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result
#
# def calculate_sum_via_args(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result
#
# def run_example():
#     numbers = [1,2,3,4,5,6]
#     result = calculate_sum_via_list(numbers)
#     print(result)
#
#     result = calculate_sum_via_args(1,2,3,4,5,6)
#     print(result)
#
# if __name__=="__main__":
#     run_example()

# def print_grade(**kwargs):
#     for subject,grade in kwargs.items():
#         print(f"Z {subject} wystawiono {grade}")
#
# def run_example():
#     print_grade(
#         matematyka=4,
#         fizyka=4,
#         chemia=5,
#         polski=4,
#         biologia=4,
#         geografia=3)
#
# if __name__=="__main__":
#     run_example()

# Można jeszcze inaczej

# def calculate_sum_via_args(*args):
#     result = 0
#     for number in args:
#         result += number
#     return result
#
# def add_two_numbers(first,second):
#     return first + second
#
# def run_example():
#     numbers = [1,2,3,4,5,6]
#     result = calculate_sum_via_args(*numbers)
#     print(result)
#
#     two_numbers = [10,30]
#     result = add_two_numbers(*two_numbers)
#     print(result)
#
#     combined_numbers = [*numbers, *two_numbers]
#     print(combined_numbers)

def print_grades(**kwargs):
    for subject, grade in kwargs.items():
        print(f"Z przedmiotu: {subject} wystawiono: {grade}")


def run_example():
    grades = {
        "matematyka": 4,
        "fizyka": 4,
        "chemia": 5,
    }

    # print_grades(grades)      to nie zadziała

#      a to za działa analogicznie do calculate_sum_via_args(*numbers)

    more_grades = {
            "polski" : 4,
            "biologia":4,
            "geografia" :3
    }


    all_grades= {**grades,**more_grades}

    print(all_grades)
if __name__=="__main__":
    run_example()

