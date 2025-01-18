from datetime import datetime

def dodaj_wpis():
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wpis = input("Wpisz treść dziennika: ")

    with open("dziennik.txt", "a") as plik:
        plik.write(f"{data}\n{wpis}\n\n")
    print("Wpis zapisany.")

def pokaz_wpisy():
    try:
        with open("dziennik.txt", "r") as plik:
            wpisy = plik.read()
            if wpisy:
                print("\nZapisane wpisy w dzienniku:")
                print(wpisy)
            else:
                print("Brak zpaisanych wpisów.")
    except FileNotFoundError:
        print("Brak zapisanych wpisów.")

while True:
    print("\nDziennik osobisty")
    print("1. Dodaj wpis")
    print("2. Wyświetl wpisy")
    print("3. Wyjście")

    wybor = input("Wybierz opcję: ")
    if wybor == '1':
        dodaj_wpis()
    if wybor == '2':
        pokaz_wpisy()
    if wybor == '3':
        print("Koniec programu.")
        break
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie")