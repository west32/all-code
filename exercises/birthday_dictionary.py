import json


def welcome(file_name):
    print(">>> Welcome to the birthday dictionary. We know the birthdays of")
    with open(file_name,"r") as data_file:
        data_dict= json.load(data_file)
    return data_dict


def print_date_of_chosen_name(data_dict):
    for key in data_dict.keys():
        print(key)
    name =input("pick name: ").title()
    if name in data_dict:
        print(f" {name}'s birthday is {data_dict[name]}")
    else:
        print("sorry this name itsn't in data")

def add_new_record(data_dict):

        name=input("enter name ")
        bday=input("eneter date of bday")
        data_dict[name]= bday
        with open("birthdays.json","w",encoding='utf-8') as data_file:
            json.dump(data_dict,data_file,indent=4)
        for key in data_dict.keys():
            print(key)



def run_exercise():
    data_dict = welcome("birthdays.json")
    print_date_of_chosen_name(data_dict)
    add_new_one =""
    while add_new_one !="E":
        add_new_one = input("Do you want to add new name?(Y/N) E- for exit").upper()
        if add_new_one == "Y":
            add_new_record(data_dict)
        elif add_new_one != "Y" and add_new_one != "N" and add_new_one!="E":
            print("choose Y or N it's that simple ;) ")
        elif add_new_one == "E":
            break
        else:
            print_date_of_chosen_name(data_dict)




run_exercise()