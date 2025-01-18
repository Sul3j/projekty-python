import random

def zgadnij_liczbe():
    liczba_do_zgadniecia = random.randint(1, 100)
    proba = 0

    print("Zgadnij liczbę od 1 do 100!")

    while True:
        proba += 1
        zgadnij = int(input("Twoja próba: "))

        if zgadnij < liczba_do_zgadniecia:
            print("Za mało!")
        elif zgadnij > liczba_do_zgadniecia:
            print("Za duzo!")
        else:
            print(f"Brawo! Odgadłeś liczbę w {proba} próbie.")

zgadnij_liczbe()