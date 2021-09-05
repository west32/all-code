


def run_example():
    workbook = load_workbook(filename="python.xlsx")
    print(workbook.sheetnames)
    first_sheet = workbook.active
    print(first_sheet)

    print(first_sheet["A1"].value, first_sheet["B1"].value)
    print(first_sheet["A1"].value, first_sheet["B2"].value)

    first_sheet["A1"].value = "Hello!"
    print(first_sheet["A1"].value)

    workbook.save(filename="updated-python.xlsx")

if __name__=="__main__":
    run_example()