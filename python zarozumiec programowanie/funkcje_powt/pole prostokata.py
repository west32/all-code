def calculate_area(a,b):
    return a * b

def ask_for_int(message):
    input_value=input(message)
    return int(input_value)

def run_are_calculator():
    a= ask_for_int('jakiej dlugosi jest bok a? ')
    b= ask_for_int('jakiej dlugosi jest bok b? ')
    area=calculate_area(a,b)
    print(f"pole prostokąta wynosi {area:.0f} cm kwadratowych")

option = None
while option != 'x':
    run_are_calculator()
    option= input("aby przerwac wcisnij 'x' aby obliczyc jeszcze raz wcisnij dowolny inny klawisz")