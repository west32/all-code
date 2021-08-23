import random


def run_example():
    # expanditures = {
    #     "prąd": [250],
    #     "woda": [30.45],
    #     "zakupy": [
    #         120.15,
    #         170.53,
    #         20.15
    #     ]
    # }

    # print(expanditures)


    # water_expenditures= expanditures.get("woda")
    # print(water_expenditures)


    # cookies_expenditures = expanditures.get("ciasteczka")
    # cookies_expenditures = expanditures["ciasteczka"]
    # cookies_expenditures = expanditures.get("ciasteczka",[10])


    # expanditures.update(woda = [95])


    # other_expenditures = {
    #     "remont": [1450],
    #     "interner": [40]
    # }
    # expanditures.update(other_expenditures)


    # expenditures_names = ["prąd", "woda","zakupy"]
    # expenditures = {expenditure_name: random.randint(1,10)for expenditure_name in expenditures_names}

    student_names = ["Alicja", "Robert", "Mikołaj", "Konstanty"]
    students = {random.randint(1,100): name for name in student_names }

    new_students = {identifier * 10 : f"{name[:1]}..."  for identifier, name in students.items()}

    # students = {
    #     random.randint(1,100): name if len(name) <8 else f"{name[:5]}..."
    #     for name in student_names }


    print(new_students)




if __name__=="__main__":
    run_example()

