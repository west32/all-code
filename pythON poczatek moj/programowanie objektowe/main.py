from shop.class_order import generate_an_order, print_order

def run_homework ():

    first_order= generate_an_order()
    print_order(first_order)
    second_order = generate_an_order()
    print_order(second_order)


if __name__ == '__main__':
    run_homework()