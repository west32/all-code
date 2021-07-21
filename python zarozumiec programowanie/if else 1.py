produkt_1 = float(input("ile kosztuje produkt nr1? "))
produkt_2 = float(input("ile kosztuje produkt nr2? "))
produkt_3 = float(input("ile kosztuje produkt nr3? "))

if produkt_1 > produkt_2:
    print("produkt 1 jest droższy od produktu 2 ")
else:
    print("Produkt 1 jest tańszy od produktu 2")
if produkt_1 > produkt_3:
    print("oraz droższy od produktu 3")
else:
    print ("oraz tańszy od produktu 3")

