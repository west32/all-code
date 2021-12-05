lower = "79-900"
upper = "80-155"

def post_code_generator(lower,upper):
    lower_int =int(lower.replace("-",""))
    upper_int = int(upper.replace("-",""))


    post_codes=[str(code) for code in range(lower_int,upper_int+1)]


    formated_post_codes=[]

    for code in post_codes:
        formated_code=f"{code[0]}{code[1]}-{code[2]}{code[3]}{code[4]}"
        formated_post_codes.append(formated_code)

    return formated_post_codes

def run_exercise_one():
    lower = "79-900"
    upper = "80-155"
    print(post_code_generator(lower,upper))

if __name__=="__main__":
    run_exercise_one()