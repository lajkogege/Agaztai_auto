def elsofeladat():
    auto_neve:str=str(input("Kérem az autó nevét: "))
    gyartasi_datum:int=int(input("Kérem a gyártási évét: "))

    print(f"I/A")
    print(f"\tAutó neve:{auto_neve}")
    print(f"\tGyártási dátum:{gyartasi_datum}")

    print("I/B")
    if gyartasi_datum == 2024:
        print(f"\tEz az {auto_neve} friss gyártás")
    elif gyartasi_datum<2000:
        print(f"\tEz az {auto_neve} öreg autó")
    else:
        print(f"\tEz az {auto_neve}  átlagos korú.")