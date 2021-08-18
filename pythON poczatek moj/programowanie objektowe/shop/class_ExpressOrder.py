
#
# Wykorzystaj metodę super do odwołania się z poziomu klasy ExpressOrder do bazowej implementacji
# metody total_price i zastąp powtórzony w klasie potomnej algorytm wynikiem z tego odwołania.
#
#
# Pamiętaj, że łączna wartość zamówienia ekspresowego to:
# łączna wartość zamówienia policzona według bazowej metody + opłata za ekspresową dostawę


from shop.class_order import Order

class ExpressOrder (Order):
    def __init__(self, delivery_date, *args,**kwargs ):
        super().__init__(*args,**kwargs)
        self.delivery_date = delivery_date

    extra_money_for_express = 15


    @property
    def total_price(self):
        return super().total_price + self.extra_money_for_express

    def __str__(self):
        gap_between = 20*"="
        orderer = f"zamówienie dla : {self.orderer_first_name} {self.orderer_last_name}"
        total = f"łączna kwota do zapłaty to: {self.total_price} PLN"
        products = "zamówione produkty:\n"
        for element in self.order_elements:
           products += f" \t {element}\n"
        delivery_date = f"Zamówienie zostanie dostarczone do odbiorcy : {self.delivery_date}"
        result =  f"\n".join((gap_between, orderer, total,  products, delivery_date, gap_between))
        return result