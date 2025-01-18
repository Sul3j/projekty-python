def szyfr_cezara():
    tekst = input("Podaj tekst do zaszyfrowania: ")
    klucz = int(input("Podaj klucz (liczbaprzesunięć): "))
    zaszyfrowany = ""

    for char in tekst:
        if char.isalpha():
            przesun = ord('a') if char.islower() else ord('A')
            zaszyfrowany += chr((ord(char) - przesun + klucz) % 26 + przesun)
        else:
            zaszyfrowany += char

    przesun(f"Zaszyfrowany tekst: {zaszyfrowany}")

szyfr_cezara()



