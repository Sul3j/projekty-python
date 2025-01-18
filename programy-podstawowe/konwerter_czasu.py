def konwerter_czasu():
    print("1. Godziny, minuty, sekundy -> sekundy")
    print("2. Sekundy -> godziny, minuty, sekundy")

    wybor = input("Wybierz opcje: ")

    if wybor == '1':
        godziny = int(input("Podaj liczbę godzin: "))
        minuty = int(input("Podaj liczbę minut: "))
        sekundy = int(input("Podaj liczbę sekund: "))
        calkowite_sekundy = godziny * 3600 + minuty * 60 + sekundy
        print(f"Łączna liczba sekund: {calkowite_sekundy}")
    elif wybor == '2':
        calkowite_sekundy = int(input("Podaj liczbę sekund: "))
        godziny = calkowite_sekundy // 3600
        minuty = (calkowite_sekundy % 3600) // 60
        sekundy = calkowite_sekundy % 60
        print(f"{godziny} godzin, {minuty} minut, {sekundy} sekund")
    else:
        print("Nieprawidłowy wybór.")

konwerter_czasu()