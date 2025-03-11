import sqlite3
import secrets
import string
import re
import base64
import hashlib
from cryptography.fernet import Fernet


def generate_key_from_password(master_password):
    hashed_pw = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hashed_pw)

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                (id INTEGER PRIMARY KEY, site TEXT, login TEXT, password TEXT)''')

def generate_password(length=16, use_digits=True, use_special=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r'\d', password) is None
    uppercase_error = re.search(r'[A-Z]', password) is None
    lowercase_error = re.search(r'[a-z]', password) is None
    symbol_error = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    strength = (5 - sum(errors)) * 20
    return strength

def add_password(site, login, password, cipher_suite):
    encrypted_password = cipher_suite.encrypt(password.encode()).decode()
    cursor.execute("INSERT INTO passwords (site, login, password) VALUES (?, ?, ?)",
                   (site, login, encrypted_password))
    conn.commit()

def get_password(site, cipher_suite):
    cursor.execute("SELECT login, password FROM passwords WHERE site=?", (site,))
    result = cursor.fetchone()
    if result:
        login, encrypted_password = result
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
        return login, decrypted_password
    else:
        return None

if __name__ == "__main__":
    site = input("Введите название сайта: ")
    login = input("Введите логин: ")
    master_password = input("Введите мастер-пароль: ")

    cipher_suite = Fernet(generate_key_from_password(master_password))

    length = int(input("Длина пароля (8-32): "))
    use_digits = input("Использовать цифры (y/n)? ").lower() == 'y'
    use_special = input("Использовать спецсимволы (y/n)? ").lower() == 'y'

    password = generate_password(length, use_digits, use_special)
    print("Сгенерированный пароль:", password)
    print("Надежность пароля:", check_strength(password), "%")

    add_password(site, login, password, cipher_suite)

    retrieved_login, retrieved_password = get_password(site, cipher_suite)
    print(f"Данные сохранены. Логин: {retrieved_login}, Пароль: {retrieved_password}")
