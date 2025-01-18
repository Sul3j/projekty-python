def przelicznik_jednostek():
    print("Przelicznik jednostek")
    print("1. Kilometry na Mile")
    print("2. Mile na Kilometry")
    print("3. Kilogramy na Funty")
    print("4. Funty na Kilogramy")

    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        km = float(input("Podaj ilość kilometrów: "))
        mile = km * 0.621371
        print(f"{km} km to {mile:.2f} mile")
    elif wybor == '2':
        mile = float(input("Podaj ilosc mil: "))
        km = mile / 0.621371
        print(f"{mile} mile to {km:.2f} km")
    elif wybor == '3':
        kg = float(input("Podaj ilosc kilogramow: "))
        funty = kg * 2.20462
        print(f"{kg} kg to {funty:.2f} funty")
    elif wybor == '4':
        funty = float(input("Podaj ilosc funtów: "))
        kg = funty / 2.20462
        print(f"{funty} funty to {kg:.2f} kg")
    else:
        print("Nieprawidłowa opcja.")

przelicznik_jednostek()