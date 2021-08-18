
# Zastąp dotychczasową implementację polityk rabatowych wykorzystującą
# funkcje rozwiązaniem opartym o klasy, dziedziczenie i polimorfizm.

# Utwórz klasę DiscountPolicy i zaimplementuj w niej metodę apply_discount
# przyjmującą wartość zamówienia i zwracającą kwotę pomniejszoną o rabat.
# W klasie DiscountPolicy metoda ta po prostu zwróci otrzymaną wartość
# tak samo jak wcześniej robiła to funkcja default_policy).


# Następnie utwórz dwie klasy dziedziczące po DiscountPolicy:
#
# PercentageDiscount, która przyjmuje w konstruktorze wartość procentową
# rabatu jaki ma udzielić i odpowiednio przelicza wartość w apply_discount.
# AbsoluteDiscount, która przyjmuje w konstruktorze wartość o którą zmniejsza
# zamówienie, dbając przy tym by zwrócony wynik nie był poniżej zera.
#
# W skrypcie main utwórz kilka wariantów zamówienia z tymi samymi produktami ale
# innymi politykami rabatowymi. Pamiętaj żeby dostosować użycie polityki rabatowej
# wewnątrz klasy Order.




# def standart_policy (total_price):
#     return total_price
#
# def loyal_policy (total_price):
#     return total_price * 0.95
#
# def christmas_policy(total_price):
#     if total_price >100:
#         return total_price - 20
#     return total_price

class DiscountPolicy:


    def apply_discount(self,total_price):
        return total_price

class PercentageDiscount(DiscountPolicy):

    def __init__(self, discount_percentage):
        self.percentage_discout = discount_percentage

    def apply_discount(self,total_price):
        return total_price *(100- self.percentage_discout)/100

class AbsoluteDiscount(DiscountPolicy):

    def __init__(self,discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self,total_price):
        result = total_price - self.discount_amount
        if result > 0:
            return result
        else:
            print ("Wartość zamówienia jest zbyt niska")









