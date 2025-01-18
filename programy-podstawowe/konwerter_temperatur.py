def konwerter_temperatury():
    print("Konwerter temperatury")
    print("1. Celsjusz na Fahrenheit")
    print("2. Fahrenheit na Celsjusz")

    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}'C to {fahrenheit}'F")
    elif wybor == '2':
        fahrenheit = float(input("Podaj temperturę w stopniach Fahrenheita: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}'F to {celsius}'C")
    else:
        print("Nieprawidłowa opcja")

konwerter_temperatury()