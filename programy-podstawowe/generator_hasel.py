import string
import random

znaki = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generowanie_hasla():
    dlugosc_hasla = int(input("Jak długie chcesz haslo: "))

    random.shuffle(znaki)

    haslo = []

    for x in range(dlugosc_hasla):
        haslo.append(random.choice(znaki))

    random.shuffle(haslo)

    haslo = "".join(haslo)

    print(f"nasze wygenerowane haslo to: {haslo}")

generowanie_hasla()