import mysql.connector
from mysql.connector import Error
import hashlib

# pip install mysql-connector-python

# Hashowanie hasła
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Połączenie z bazą danych
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="admin",      
            password="password",  
            database="sklep"
        )
        return connection
    except Error as e:
        print(f"Błąd podczas łączenia z bazą danych: {e}")
        return None

# Tworzenie wymaganych tabel
def create_tables(connection):
    cursor = connection.cursor()
    queries = [
        """
        CREATE TABLE IF NOT EXISTS pracownicy (
            id INT AUTO_INCREMENT PRIMARY KEY,
            imie VARCHAR(255) NOT NULL,
            nazwisko VARCHAR(255) NOT NULL,
            login VARCHAR(255) UNIQUE NOT NULL,
            haslo VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS klienci (
            id INT AUTO_INCREMENT PRIMARY KEY,
            imie VARCHAR(255) NOT NULL,
            nazwisko VARCHAR(255) NOT NULL,
            login VARCHAR(255) UNIQUE NOT NULL,
            haslo VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS produkty (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nazwa VARCHAR(255) NOT NULL,
            ilosc INT NOT NULL,
            cena DECIMAL(10, 2) NOT NULL,
            id_pracownika INT,
            FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS sprzedaze (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_produktu INT,
            id_klienta INT,
            ilosc INT NOT NULL,
            data_sprzedazy TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_produktu) REFERENCES produkty(id),
            FOREIGN KEY (id_klienta) REFERENCES klienci(id)
        )
        """
    ]
    for query in queries:
        cursor.execute(query)
    connection.commit()

# Rejestracja użytkownika (pracownik lub klient)
def register_user(connection, table):
    imie = input(f"Podaj imię ({table}): ")
    nazwisko = input(f"Podaj nazwisko ({table}): ")
    login = input(f"Podaj login ({table}): ")
    password = input("Podaj hasło: ")
    hashed_password = hash_password(password)
    
    query = f"INSERT INTO {table} (imie, nazwisko, login, haslo) VALUES (%s, %s, %s, %s)"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (imie, nazwisko, login, hashed_password))
        connection.commit()
        print(f"Rejestracja zakończona sukcesem dla {table}!")
    except Error as e:
        print(f"Błąd podczas rejestracji: {e}")

# Logowanie użytkownika (pracownik lub klient)
def login_user(connection, table):
    login = input(f"Podaj login ({table}): ")
    password = input("Podaj hasło: ")
    hashed_password = hash_password(password)
    
    query = f"SELECT id FROM {table} WHERE login = %s AND haslo = %s"
    cursor = connection.cursor()
    cursor.execute(query, (login, hashed_password))
    result = cursor.fetchone()
    
    if result:
        print(f"Zalogowano jako {table}: {login}")
        return result[0]  # Zwraca ID użytkownika
    else:
        print("Nieprawidłowy login lub hasło.")
        return None

# Dodanie produktu
def add_product(connection, worker_id):
    nazwa = input("Podaj nazwę produktu: ")
    ilosc = int(input("Podaj ilość: "))
    cena = float(input("Podaj cenę: "))
    
    query = "INSERT INTO produkty (nazwa, ilosc, cena, id_pracownika) VALUES (%s, %s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(query, (nazwa, ilosc, cena, worker_id))
    connection.commit()
    print("Produkt został dodany!")

# Wyświetlanie produktów
def display_products(connection):
    query = "SELECT * FROM produkty"
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    
    if not results:
        print("Brak produktów w hurtowni.")
    else:
        print("\nLista produktów:")
        print(f"{'ID':<5}{'Nazwa':<20}{'Ilość':<10}{'Cena':<10}")
        for row in results:
            print(f"{row[0]:<5}{row[1]:<20}{row[2]:<10}{row[3]:<10}")

# Zakup produktu
def purchase_product(connection, client_id):
    display_products(connection)
    product_id = int(input("Podaj ID produktu do zakupu: "))
    ilosc = int(input("Podaj ilość do zakupu: "))
    
    cursor = connection.cursor()
    # Sprawdzanie dostępności
    query = "SELECT ilosc FROM produkty WHERE id = %s"
    cursor.execute(query, (product_id,))
    result = cursor.fetchone()
    
    if result and result[0] >= ilosc:
        # Aktualizacja stanu produktu
        update_query = "UPDATE produkty SET ilosc = ilosc - %s WHERE id = %s"
        cursor.execute(update_query, (ilosc, product_id))
        
        # Rejestracja zakupu
        insert_query = "INSERT INTO sprzedaze (id_produktu, id_klienta, ilosc) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (product_id, client_id, ilosc))
        connection.commit()
        print("Zakup zakończony sukcesem!")
    else:
        print("Brak wystarczającej ilości produktu.")

# Wyświetlanie historii sprzedaży
def view_sales_history(connection):
    query = """
        SELECT 
            sprzedaze.id AS id_sprzedazy,
            produkty.nazwa AS produkt,
            produkty.cena AS cena,
            klienci.imie AS klient_imie,
            klienci.nazwisko AS klient_nazwisko,
            sprzedaze.ilosc AS ilosc_sprzedana,
            sprzedaze.data_sprzedazy AS data
        FROM sprzedaze
        JOIN produkty ON sprzedaze.id_produktu = produkty.id
        JOIN klienci ON sprzedaze.id_klienta = klienci.id
        ORDER BY sprzedaze.data_sprzedazy DESC
    """
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    print(results)
    
    if not results:
        print("Brak zapisanej historii sprzedaży.")
    else:
        print("\nHistoria sprzedaży:")
        print(f"{'ID':<5}{'Produkt':<20}{'Cena':<10}{'Klient':<25}{'Ilość':<10}{'Data':<20}")
        for row in results:
            id_sprzedazy, produkt, cena, klient_imie, klient_nazwisko, ilosc, data = row
            klient = f"{klient_imie} {klient_nazwisko}"
            print(f"{id_sprzedazy:<5}{produkt:<20}{cena:<10}{klient:<25}{ilosc:<10}{data.strftime("%d-%m-%Y")}")


# Główna pętla programu
def main():
    connection = connect_to_database()
    if connection is None:
        print("Nie udało się połączyć z bazą danych. Zamykanie programu.")
        return
    
    create_tables(connection)
    
    while True:
        print("\n--- Hurtownia ---")
        print("1. Rejestracja (pracownik)")
        print("2. Logowanie (pracownik)")
        print("3. Rejestracja (klient)")
        print("4. Logowanie (klient)")
        print("5. Wyjście")
        
        choice = input("Wybierz opcję: ")
        
        if choice == "1":
            register_user(connection, "pracownicy")
        elif choice == "2":
            worker_id = login_user(connection, "pracownicy")
            if worker_id:
                while True:
                    print("\n--- Panel Pracownika ---")
                    print("1. Dodaj produkt")
                    print("2. Wyświetl produkty")
                    print("3. Wyświetl historię sprzedaży")
                    print("4. Wyloguj")
                    worker_choice = input("Wybierz opcję: ")
                    if worker_choice == "1":
                        add_product(connection, worker_id)
                    elif worker_choice == "2":
                        display_products(connection)
                    elif worker_choice == "3":
                        view_sales_history(connection)
                    elif worker_choice == "4":
                        break
        elif choice == "3":
            register_user(connection, "klienci")
        elif choice == "4":
            client_id = login_user(connection, "klienci")
            if client_id:
                while True:
                    print("\n--- Panel Klienta ---")
                    print("1. Wyświetl produkty")
                    print("2. Kup produkt")
                    print("3. Wyloguj")
                    client_choice = input("Wybierz opcję: ")
                    if client_choice == "1":
                        display_products(connection)
                    elif client_choice == "2":
                        purchase_product(connection, client_id)
                    elif client_choice == "3":
                        break
        elif choice == "5":
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

    if connection.is_connected():
        connection.close()
        print("Połączenie z bazą danych zostało zamknięte.")

if __name__ == "__main__":
    main()