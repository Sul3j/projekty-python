def kalkulator_sredniej():
    liczby = input("Podaj liczby oddzielone spacją: ")
    liczby = [float(x) for x in liczby.split()]
    srednia = sum(liczby) / len(liczby)
    print(f"Śrenia arytmetyczna: {srednia:.2f}")

kalkulator_sredniej()