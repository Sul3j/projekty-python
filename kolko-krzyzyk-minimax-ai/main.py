import sys
import pygame
import numpy as np

# pip install pygame
# pip install numpy

# Inicjalizacja biblioteki Pygame, która będzie używana do renderowania gry.
pygame.init()

# Definicja kolorów w formacie RGB.
BIALY = (255, 255, 255)
SZARY = (180, 180, 180)
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
CZARNY = (0, 0, 0)

# Ustawienia proporcji i rozmiarów planszy oraz elementów gry.
SZEROKOSC = 300  # Szerokość okna gry
WYSOKOSC = 300  # Wysokość okna gry
SZEROKOSC_LINII = 5  # Grubość linii siatki
WIERSZE = 3  # Liczba wierszy na planszy
KOLUMNY = 3  # Liczba kolumn na planszy
ROZMIAR_KWADRATU = SZEROKOSC // KOLUMNY  # Rozmiar jednego kwadratu na planszy
PROMIEN_KOLA = ROZMIAR_KWADRATU // 3  # Promień kółka
SZEROKOSC_KOLA = 15  # Grubość linii kółka
SZEROKOSC_KRZYZYKA = 25  # Grubość linii krzyżyka

# Tworzenie okna gry i ustawienie jego parametrów.
okno = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption('Kolko Krzyzyk AI')
okno.fill(CZARNY)  # Wypełnienie tła kolorem czarnym

# Inicjalizacja planszy jako 3x3 tablica wypełniona zerami.
plansza = np.zeros((WIERSZE, KOLUMNY))

# Funkcja rysująca linie siatki planszy gry.
def rysuj_linie(kolor=BIALY):
    for i in range(1, WIERSZE):
        # Rysowanie poziomych linii
        pygame.draw.line(okno, kolor, (0, ROZMIAR_KWADRATU * i), (SZEROKOSC, ROZMIAR_KWADRATU * i), SZEROKOSC_LINII)
        # Rysowanie pionowych linii
        pygame.draw.line(okno, kolor, (ROZMIAR_KWADRATU * i, 0), (ROZMIAR_KWADRATU * i, WYSOKOSC), SZEROKOSC_LINII)

# Funkcja rysująca figury (kółko lub krzyżyk) na planszy.
def rysuj_figury(kolor=BIALY):
    for wiersz in range(WIERSZE):
        for kolumna in range(KOLUMNY):
            if plansza[wiersz][kolumna] == 1:
                # Rysowanie kółka
                pygame.draw.circle(okno, kolor, (int(kolumna * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU // 2), int(wiersz * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU // 2)), PROMIEN_KOLA, SZEROKOSC_KOLA)
            elif plansza[wiersz][kolumna] == 2:
                # Rysowanie krzyżyka
                pygame.draw.line(okno, kolor, (kolumna * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU // 4, wiersz * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU // 4), (kolumna * ROZMIAR_KWADRATU + 3 * ROZMIAR_KWADRATU // 4, wiersz * ROZMIAR_KWADRATU + 3 * ROZMIAR_KWADRATU // 4), SZEROKOSC_KRZYZYKA)
                pygame.draw.line(okno, kolor, (kolumna * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU // 4, wiersz * ROZMIAR_KWADRATU + 3 * ROZMIAR_KWADRATU // 4), (kolumna * ROZMIAR_KWADRATU + 3 * ROZMIAR_KWADRATU // 4, wiersz * ROZMIAR_KWADRATU + ROZMIAR_KWADRATU // 4), SZEROKOSC_KRZYZYKA)

# Funkcja oznaczająca kwadrat na planszy dla danego gracza.
def zaznacz_kwadrat(wiersz, kolumna, gracz):
    plansza[wiersz][kolumna] = gracz

# Funkcja sprawdzająca, czy dany kwadrat na planszy jest dostępny.
def dostepny_kwadrat(wiersz, kolumna):
    return plansza[wiersz][kolumna] == 0

# Funkcja sprawdzająca, czy plansza jest pełna (wszystkie kwadraty zajęte).
def czy_pelna_plansza(sprawdz_plansze=plansza):
    for wiersz in range(WIERSZE):
        for kolumna in range(KOLUMNY):
            if sprawdz_plansze[wiersz][kolumna] == 0:
                return False
    return True

# Funkcja sprawdzająca, czy dany gracz wygrał grę.
def sprawdz_wygrana(gracz, sprawdz_plansze=plansza):
    # Sprawdzenie kolumn
    for kolumna in range(KOLUMNY):
        if sprawdz_plansze[0][kolumna] == gracz and sprawdz_plansze[1][kolumna] == gracz and sprawdz_plansze[2][kolumna] == gracz: 
            return True
    # Sprawdzenie wierszy
    for wiersz in range(WIERSZE):
        if sprawdz_plansze[wiersz][0] == gracz and sprawdz_plansze[wiersz][1] == gracz and sprawdz_plansze[wiersz][2] == gracz: 
            return True
    # Sprawdzenie przekątnych
    if sprawdz_plansze[0][0] == gracz and sprawdz_plansze[1][1] == gracz and sprawdz_plansze[2][2] == gracz:
        return True
    if sprawdz_plansze[0][2] == gracz and sprawdz_plansze[1][1] == gracz and sprawdz_plansze[2][0] == gracz:
        return True
    return False

# Funkcja implementująca algorytm Minimax z obcinaniem alfa-beta.
def minimax(minimax_plansza, glebokosc, maksymalizujacy, alfa=-float('inf'), beta=float('inf')):
    # Sprawdzenie stanu gry
    if sprawdz_wygrana(2, minimax_plansza):
        return 10 - glebokosc
    elif sprawdz_wygrana(1, minimax_plansza):
        return glebokosc - 10
    elif czy_pelna_plansza(minimax_plansza):
        return 0

    # Ograniczenie głębokości rekursji
    if glebokosc == 5:
        return 0

    if maksymalizujacy:
        najlepszy_wynik = -float('inf')
        for wiersz in range(WIERSZE):
            for kolumna in range(KOLUMNY):
                if minimax_plansza[wiersz][kolumna] == 0:
                    minimax_plansza[wiersz][kolumna] = 2
                    wynik = minimax(minimax_plansza, glebokosc + 1, False, alfa, beta)
                    minimax_plansza[wiersz][kolumna] = 0
                    najlepszy_wynik = max(wynik, najlepszy_wynik)
                    alfa = max(alfa, wynik)
                    if beta <= alfa:
                        break
        return najlepszy_wynik
    else:
        najlepszy_wynik = float('inf')
        for wiersz in range(WIERSZE):
            for kolumna in range(KOLUMNY):
                if minimax_plansza[wiersz][kolumna] == 0:
                    minimax_plansza[wiersz][kolumna] = 1
                    wynik = minimax(minimax_plansza, glebokosc + 1, True, alfa, beta)
                    minimax_plansza[wiersz][kolumna] = 0
                    najlepszy_wynik = min(wynik, najlepszy_wynik)
                    beta = min(beta, wynik)
                    if beta <= alfa:
                        break
        return najlepszy_wynik

# Funkcja znajdująca najlepszy ruch dla komputera (gracz 2).
def najlepszy_ruch():
    najlepszy_wynik = -float('inf')
    ruch = (-1, -1)
    for wiersz in range(WIERSZE):
        for kolumna in range(KOLUMNY):
            if plansza[wiersz][kolumna] == 0:
                plansza[wiersz][kolumna] = 2
                wynik = minimax(plansza, 0, False)
                plansza[wiersz][kolumna] = 0
                if wynik > najlepszy_wynik:
                    najlepszy_wynik = wynik
                    ruch = (wiersz, kolumna)
                # Dodatkowa losowość przy równych wynikach
                elif wynik == najlepszy_wynik and np.random.rand() < 0.5:
                    ruch = (wiersz, kolumna)
    
    if ruch != (-1, -1):
        zaznacz_kwadrat(ruch[0], ruch[1], 2)
        return True
    return False

# Funkcja restartująca grę i czyszcząca planszę.
def restartuj_gre():
    okno.fill(CZARNY)
    rysuj_linie()
    for wiersz in range(WIERSZE):
        for kolumna in range(KOLUMNY):
            plansza[wiersz][kolumna] = 0

# Rysowanie początkowej siatki gry.
rysuj_linie()

gracze = 1  # Ustawienie początkowego gracza na gracza 1 (kółko)
gra_skonczona = False  # Flaga do śledzenia zakończenia gry

# Pętla główna gry obsługująca zdarzenia i aktualizacje ekranu.
while True:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            sys.exit()  # Zamyka grę

        if zdarzenie.type == pygame.MOUSEBUTTONDOWN and not gra_skonczona:
            myszX = zdarzenie.pos[0] // ROZMIAR_KWADRATU
            myszY = zdarzenie.pos[1] // ROZMIAR_KWADRATU

            if dostepny_kwadrat(myszY, myszX):
                zaznacz_kwadrat(myszY, myszX, gracze)
                if sprawdz_wygrana(gracze):
                    gra_skonczona = True
                gracze = gracze % 2 + 1

                if not gra_skonczona:
                    if najlepszy_ruch():
                        if sprawdz_wygrana(2):
                            gra_skonczona = True
                        gracze = gracze % 2 + 1

                if not gra_skonczona:
                    if czy_pelna_plansza():
                        gra_skonczona = True

        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_r:
                restartuj_gre()
                gra_skonczona = False
                gracze = 1

    # Rysowanie figur i aktualizacja ekranu.
    if not gra_skonczona:
        rysuj_figury()
    else:
        if sprawdz_wygrana(1):
            rysuj_figury(ZIELONY)
            rysuj_linie(ZIELONY)
        elif sprawdz_wygrana(2):
            rysuj_figury(CZERWONY)
            rysuj_linie(CZERWONY)
        else:
            rysuj_figury(SZARY)
            rysuj_linie(SZARY)

    pygame.display.update()  # Aktualizacja okna gry
