numer_telefonu = input("Podaj swój numer telefonu:")
numer_telefonu = numer_telefonu.replace('-', '')
publiczne_cyfry = numer_telefonu[:5]
ilosc_prywatnych_cyfr = len(numer_telefonu) -5
prywatne_cyfry = "-" * ilosc_prywatnych_cyfr
anonimowy_numer = publiczne_cyfry + prywatne_cyfry
print(anonimowy_numer)