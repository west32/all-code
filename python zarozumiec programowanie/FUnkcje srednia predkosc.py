# Napisz funkcję liczącą prędkość średnią na podstawie zadanego dystansu i czasu.
#
# Następnie wykorzystaj ją implementując program, który wyznaczy:
#
# średnią prędkość biegu
# średnią prędkość jazdy na rowerze
# średnią prędkość jazdy autem

def zapytaj_o_wartosc_float (wiadomosc):
    input_wartosc = input(wiadomosc)
    return float(input_wartosc)
def oblicz_srednią_prędkosc (dystans,czas):
    return dystans / czas

#
# bieg_dyst= zapytaj_o_wartosc_float("ile przebiegłeś?")
# bieg_czas= zapytaj_o_wartosc_float('w jakim czsie (w godzinach)?')
# rower_dyst= zapytaj_o_wartosc_float('jaki dystans przebyles na rowerze?')
# rower_czas= zapytaj_o_wartosc_float('ile godzin Ci to zajeło')
# auto_dyst= zapytaj_o_wartosc_float("ile przejechałęs autem")
# auto_czas= zapytaj_o_wartosc_float('ile Ci to zajeło w godzinach')
#
# print (f"Twoja średnia prędkość podczas biegu to {oblicz_srednią_prędkosc(bieg_dyst,bieg_czas)}km\h")
#
# print (f"Twoja średnia prędkość jazdy na rowerze to {oblicz_srednią_prędkosc(rower_dyst,rower_czas):.1f} km\h")
#
# print (f"Twoja średnia prędkość podczas jazdy autem to {oblicz_srednią_prędkosc(auto_dyst,auto_czas):.2f}km\h")

#lub


def run_avf_calculator (rodzaj):
    dystans= zapytaj_o_wartosc_float(f"ile km przebyles przemieszczając sie {rodzaj}")
    czas= zapytaj_o_wartosc_float("ile ci to zajeło?")
    oblicz_srednią_prędkosc(dystans,czas)
    print(f"Twoja średnia prędkość podczas {rodzaj} to {oblicz_srednią_prędkosc(dystans, czas):.1f}km\h")

run_avf_calculator("biegu")
run_avf_calculator("rowerem")
run_avf_calculator("autem")