import matplotlib.pyplot as plt
from datetime import datetime
# pip install matplotlib

def wczytaj_dane_temperatury():
    daty = []
    temperatury = []

    try:
        with open("temperatura.txt", "r") as plik:
            for linia in plik:
                dane = linia.strip().split()
                if len(dane) == 3:
                    data_czas = f"{dane[0]} {dane[1]}"
                    temperatura = float(dane[2])
                    # Konwertujemy datę i godzinę na format datetime dla poprawnego wykresu
                    daty.append(datetime.strptime(data_czas, "%Y-%m-%d %H:%M"))
                    temperatury.append(temperatura)
    except FileNotFoundError:
        print("Plik 'temperatura.txt' nie został znaleziony.")
    except ValueError:
        print("Błąd w formacie danych w pliku.")

    return daty, temperatury

def generuj_wykres(daty, temperatury):
    # Tworzymy nową figurę (obszar wykresu) o wymiarach 10x5 cali
    plt.figure(figsize=(10, 5))

    # Rysujemy wykres liniowy z danymi na osi X (daty) i Y (temperatury)
    # marker='o' - ustawia znacznik w postaci kółka dla kadego punktu na wykresie
    # color='b' - oznacza kolor niebieski dla linii i punktów
    # linestyle='-' - ustawia linię ciągłą między punktami
    plt.plot(daty, temperatury, marker='o', color='b', linestyle='-')

    # ustawiamy tytuł wykresu
    plt.title("Wykres temperatury w czasie")

    # Opis osi X, tutaj wyświetlamy datę i godzinę
    plt.xlabel("Data i godzina")

    # Opis osi Y, wyraony w stopniach celsjusza
    plt.ylabel("Temperatura (C')")

    # Dodajemy siatkę do wykresu, aby ułatwić odczytanie wartości
    plt.grid(True)

    # Ustawiamy rotację etykiet na osi X o 45 stopni, aby lepiej mieściły się na osi
    plt.xticks(rotation=45)

    # Optymalizujemy układ wykresu, aby wszystkie elementy mieściły się na rysunku
    plt.tight_layout()

    # wyświetlamy gotowy wykres na ekranie
    plt.show()

daty, temperatury = wczytaj_dane_temperatury()
if daty and temperatury:
    generuj_wykres(daty, temperatury)
else:
    print("Brak danych do wygenerowania wykrsu.")