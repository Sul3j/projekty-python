import random

wyjscie = False
punkty_gracza = 0
punkty_komputera = 0

while wyjscie == False:
    opcje = ["kamien", "papier", "nozyce"]
    wybor_gracza = input("Wybierz kamien, papier, nozyce lub wyjdz (x): ")
    wybor_komputera = random.choice(opcje)

    if wybor_gracza == 'x':
        print("Gra zostala przerwana")
        print("Uzyskales " + str(punkty_gracza) + ' punktow, a komputer zdobyl ' + str(punkty_komputera) + ' punktow')
        wyjscie = True

    if wybor_gracza == 'kamien':
        if wybor_komputera == 'kamien':
            print("Twoj wybor to kamien")
            print("Komputer wybral kamien")
            print("Mamy remis!")
        elif wybor_komputera == 'papier':
            print("Twoj wybor to kamien")
            print("Komputer wybral papier")
            print("Komputer wygral!")
            punkty_komputera += 1
        elif wybor_komputera == 'nozyce':
            print("Twoj wybor to kamien")
            print("Komputer wybral nozyce")
            print("Wygrales!")
            punkty_gracza += 1
    elif wybor_gracza == 'papier':
        if wybor_komputera == 'kamien':
            print("Twoj wybor to papier")
            print("Komputer wybral kamien")
            print("Wygrales!")
            punkty_gracza += 1
        elif wybor_komputera == 'papier':
            print("Twoj wybor to papier")
            print("Komputer wybral papier")
            print("Mamy remis!")
        elif wybor_komputera == 'nozyce':
            print("Twoj wybor to papier")
            print("Komputer wybral nozyce")
            print("Komputer wygral!")
            punkty_komputera += 1
    elif wybor_gracza == 'nozyce':
        if wybor_komputera == 'kamien':
            print("Twoj wybor to nozyce")
            print("Komputer wybral kamien")
            print("Komputer wygral!")
            punkty_komputera += 1
        elif wybor_komputera == 'papier':
            print("Twoj wybor to nozyce")
            print("Komputer wybral papier")
            print("Wygrales!")
            punkty_gracza += 1
        elif wybor_komputera == 'nozyce':
            print("Twoj wybor to nozyce")
            print("Komputer wybral nozyce")
            print("Mamy remis!")