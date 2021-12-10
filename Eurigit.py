from module1 import*
riik_dict={"Austria": "Viin",# Loo tühi sõna Capital
           "Estonia":"Tallinn",
                 "Belgia": "Brüssel",
                "Saksamaa":" Berliin",
                 "Iirimaa": "Dublin",
                 "Liechtenstein": "Vaduz",# Täitke see mitu tähendust
                "Holland": "Amsterdam",
                 "Prantsusmaa":"Pariis",
                 "Bulgaaria": "Sofia",
                 "Poola":" Varssavi",
                 "Tšehhi" : "Praha",
                 "Albaania": "Tirana",
                 "Bosnia ja Hertsegoviina": "Sarajevo",
                 "Serbia ":" Belgrad"}
print(riik_dict )
while True:
    print("kontrollige teadmisi tähtedest ja nende pealinnadest")
    print("1 - leida riik selle pealinna järgi ja vastupidi,\n2 - Lisage uus riik ja pealinn,")
    menu=input()
    if menu=="1":
        v=input("Otsime riiki pealinna järgi(1) või pealinn riigiti(2)? ")
        riik(riik_dict,v)
    elif menu=="2":
        new_key_value(riik_dict)