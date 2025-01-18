def pokaz_zadania():
    try:
        with open("lista_zadan.txt", "r") as plik:
            zadania = plik.readlines()
            if zadania:
                print("\nTwoje zadania:")
                for i, zadanie in enumerate(zadania, start=1):
                    print(f"{i}. {zadanie.strip()}")
            else:
                print("\nBrak zadań.")
    except FileNotFoundError:
        print("\nBrak zadań. Plik jeszcze nie istnieje.")

def dodaj_zadanie():
    zadanie = input("Wpisz nowe zadanie: ")
    with open("lista_zadan.txt", "a") as plik:
        plik.write(zadanie + '\n')
    print("Dodano zadanie")

def usun_zadanie():
    pokaz_zadania()
    numer_zadania = int(input("Wpisz numer zadania do usunięcia: "))
    with open("lista_zadan.txt", "r") as plik:
        zadania = plik.readlines()
    
    if 0 < numer_zadania <= len(zadania):
        zadania.pop(numer_zadania - 1)
        with open("lista_zadan.txt", "w") as plik:
            plik.writelines(zadania)
        print("Zadanie usunięte.")
    else:
        print("Nieprawidłowy numer zadania.")


while True:
    print("\nLista zadań")
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjście")

    wybor = input("Wybierz opcję: ")
    if wybor == '1':
        pokaz_zadania()
    elif wybor == '2':
        dodaj_zadanie()
    elif wybor == '3':
        usun_zadanie()
    elif wybor == '4':
        print("Koniec programu.")
        break
    else:
        print("Nieprawiłowa opcja, spróbuj ponownie.")