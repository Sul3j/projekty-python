import sqlite3
from getpass import getpass
import hashlib

# Utworzenie bazy danych
conn = sqlite3.connect('quiz_game.db')
cursor = conn.cursor()

# Tworzenie tabel
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            score INTEGER DEFAULT 0
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id)
)''')

conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Podaj nazwę uzytkownika: ")
    password = getpass("Podaj haslo: ")
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("Rejestracja zakonczona sukcesem!")
    except sqlite3.IntegrityError:
        print("Nazwa uzytkownika juz istnieje")

def login():
    username = input("Podaj swoją nazwę uzytkownika: ")
    password = getpass("Podaj haslo: ")
    hashed_password = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print("Logowanie zakończone sukcesem!")
        return user
    else:
        print("Nieprawidłowe dane logowania")
        return None
    
def add_quiz():
    name = input("Podaj nazwę quizu: ")
    try:
        cursor.execute("INSERT INTO quizzes (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Quiz '{name}' został utworzony!")
    except sqlite3.IntegrityError:
        print("Nazwa quizu juz istnieje!")

def add_question():
    cursor.execute("SELECT * FROM quizzes")
    quizzes = cursor.fetchall()
    if not quizzes:
        print("Brak dostępnych quizow. Najpierw stwórz quiz.")
        return
    
    print("Dostępne quizy:")
    for quiz in quizzes:
        print(f"{quiz[0]}: {quiz[1]}")

    quiz_id = int(input("Podaj ID quizu, do którego chcesz dodać pytanie: "))
    question = input("Wpisz pytanie: ")
    option_a = input("Wpisz opcję A: ")
    option_b = input("Wpisz opcję B: ")
    option_c = input("Wpisz opcję C: ")
    option_d = input("Wpisz opcję D: ")
    correct_option = input("Podaj poprwną opcję (A/B/C/D): ").upper()

    if correct_option not in ['A', 'B', 'C', 'D']:
        print("Niepoprawna opcja. Poprawną ocją musi być A, B, C lub D.")
        return
    
    cursor.execute("INSERT INTO questions (quiz_id, question, option_a, option_b, option_c, option_d, correct_option) VALUES (?, ?, ?, ?, ?, ?, ?)", (quiz_id, question, option_a, option_b, option_c, option_d, correct_option))
    conn.commit()
    print("Pytanie zostało dodane")

def play_quiz(user):
    cursor.execute("SELECT * FROM quizzes")
    quizzes = cursor.fetchall()
    if not quizzes:
        print("Brak dostępnych quizow. Najpierw stwórz quiz.")
        return
    
    print("Dostępne quizy:")
    for quiz in quizzes:
        print(f"{quiz[0]}: {quiz[1]}")
    
    quiz_id = int(input("Podaj ID quizu, który chcesz rozwiązać: "))
    cursor.execute("SELECT * FROM questions WHERE quiz_id = ?", (quiz_id,))
    questions = cursor.fetchall()
    if not questions:
        print("Brak pytań w tym quizie")
        return
    
    score = 0
    for q in questions:
        print(q[2])
        print(f"A: {q[3]}  B: {q[4]}  C: {q[5]}  D: {q[6]}")
        answer = input("Twoja odpowiedź (A/B/C/D): ").upper()
        if answer == q[7]:
            print("Dobrze!")
            score += 1
        else:
            print(f"Źle! Poprawna odpowiedź to {q[7]}")

    print(f"Twój wynik: {score} z {len(questions)}.")
    cursor.execute("UPDATE users SET score = score + ? WHERE id = ?", (score, user[0]))
    conn.commit()

def show_top10():
    cursor.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
    top_users = cursor.fetchall()
    print("Top 10 graczy")
    for i, user in enumerate(top_users, start=1):
        print(f"{i}. {user[0]} - {user[1]} punktów")

    
def main():
    while True:
        print("\nWitaj w grze Qiuz")
        print("1. Rejestracja")
        print("2. Logowanie")
        print("3. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n1. Rozwiąz quiz")
                    print("2. Dodaj quiz")
                    print("3. Dodaj pytanie")
                    print("4. Pokaz top 10 graczy")
                    print("5. Wyloguj się")
                    user_choice = input("Wybierz opcję: ")
                    if user_choice == "1":
                        play_quiz(user)
                    elif user_choice == "2":
                        add_quiz()
                    elif user_choice == "3":
                        add_question()
                    elif user_choice == "4":
                        show_top10()
                    elif user_choice == "5":
                        break
                    else:
                        print("Nieprawidłowa opcja. Spróbuj ponownie.")
        
        elif choice == "3":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja, Spróbuj ponownie")


if __name__ == "__main__":
    main()