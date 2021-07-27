from shop.class_order import generate_an_order
from shop.class_apple import Apple



def run_homework ():

    green_apple = Apple (species_name="green",size="small",prize_per_kg=3)
    print(f"8 kg zielonych jabłek kosztuje: {green_apple.count_total_apple_prize(8)}pln")
    red_apple = Apple (species_name="red", size="bif", prize_per_kg=5)
    print(f"5 kg czerwonych jabłek kosztuje: {red_apple.count_total_apple_prize(5)}pln ")

    first_order= generate_an_order()
    first_order.print_self()
    second_order = generate_an_order()
    second_order.print_self()


if __name__ == '__main__':
    run_homework()