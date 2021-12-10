from module1 import*
riik_dict={"Austria": "Viin",
                 "Belgia": "Brüssel",
                "Saksamaa":" Berliin",
                 "Iirimaa": "Dublin",
                 "Liechtenstein": "Vaduz",
                "Holland": "Amsterdam",
                 "Prantsusmaa":"Pariis",
                 "Bulgaaria": "Sofia",
                 "Польша": "Варшава",
                 "Чехия": "Прага",
                 "Албания": "Тирана",
                 "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье",
                 "Сербия": "Белград"}
print(riik_dict )
while True:
    print("Привет! Пройдёмся по странам и их столицам!")
    print("1 - bUurige välja riigi pealinn või vastupidi,\n2 - Lisage uus riik ja pealinn,")
    menu=input()
    if menu=="1":
        v=input("Будем искать страну по стoлице(1) или стoлицу по стране(2)? ")
        riik(riik_dict,v)
    elif menu=="2":
        new_key_value(riik_dict)