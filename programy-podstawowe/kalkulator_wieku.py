from datetime import datetime

def kalkulator_wieku():
    data_urodzenia = input("Podaj swoją datę urodzenia (RRRR-MM-DD): ")
    data_urodzenia = datetime.strptime(data_urodzenia, "%Y-%m-%d")
    dzisiaj = datetime.today()
    wiek = dzisiaj.year - data_urodzenia.year - ((dzisiaj.month, dzisiaj.day) < (data_urodzenia.month, data_urodzenia.day))
    print(f"Twój wiek to: {wiek} lat")

kalkulator_wieku()