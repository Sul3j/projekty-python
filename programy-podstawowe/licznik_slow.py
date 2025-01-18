def licznik_slow():
    tekst = input("Podaj tekst: ")
    slowa = tekst.split()
    liczba_slow = len(slowa)
    print(f"Liczba słów w tekście: {liczba_slow}")

licznik_slow()