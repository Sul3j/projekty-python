import random

def dodaj_pytanie():
    pytanie = input("Wypisz pytanie: ")
    odpowiedz = input("Wpisz poprawną odpowiedź: ")

    with open("quiz.txt", "a") as plik:
        plik.write(f"{pytanie},{odpowiedz}\n")
    print("Pytanie dodane do quizu.")

def przeprowadz_quiz():
    try:
        with open("quiz.txt", "r") as plik:
            pytania = [linia.strip().split(',') for linia in plik.readlines()]
            if not pytania:
                print("Brak pytań w quizie.")
                return
            
            random.shuffle(pytania)
            wynik = 0

            for pytanie, odpowiedz in pytania:
                odpowiedz_uzytkownika = input(f"{pytanie} ")
                if odpowiedz_uzytkownika.lower() == odpowiedz.lower():
                    print("Poprawna odpowiedź!")
                    wynik += 1
                else:
                    print(f"Błędna odpowiedź. Poprawna odpowiedź to: {odpowiedz}")

            print(f"\nTwój wynik to: {wynik}/{len(pytania)}")
        
    except FileNotFoundError:
        print("Brak pytań w quizie")


# pytanie, odpowiedz
# pytanie, odpowiedz
# pytanie, odpowiedz

# pytania = [["pytanie", "odpowiedz"], ["pytanie", "odpowiedz"]]

while True:
    print("\nQuiz wiedzy")
    print("1. Dodaj pytanie do quizu")
    print("2. Rozpocznij quiz")
    print("3. Wyjście")

    wybor = input("Wybierz opcję: ")
    if wybor == '1':
        dodaj_pytanie()
    elif wybor == '2':
        przeprowadz_quiz()
    elif wybor == '3':
        print("Koniec programu.")
        break
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")