# def zapytaj_o_wartosc_float (wiadomosc):
#     input_wartosc = input(wiadomosc)
#     return float(input_wartosc)
def oblicz_srednią_prędkosc (dystans,czas):
    return dystans / czas

def run_avf_calculator (rodzaj, dystans, czas):
    # dystans= zapytaj_o_wartosc_float(f"ile km przebyles przemieszczając sie {rodzaj}")
    # czas= zapytaj_o_wartosc_float("ile ci to zajeło?")
    oblicz_srednią_prędkosc(dystans,czas)
    print(f"Twoja średnia prędkość podczas {rodzaj} to {oblicz_srednią_prędkosc(dystans, czas):.1f}km\h")

run_avf_calculator(rodzaj="biegu", dystans=21, czas=2)
run_avf_calculator(rodzaj="rowerem", dystans=30, czas= 1.5)
run_avf_calculator(rodzaj="autem", dystans=100,czas=2)