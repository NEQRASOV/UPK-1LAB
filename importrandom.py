import random
import string

def generate_password():
    while True:
        length = random.randint(8, 32)  # случайная длина пароля от 8 до 32 символов

        # Создаем список всех символов, которые могут использоваться в пароле
        characters = string.asciiletters + string.digits + string.punctuation

        # Генерируем пароль, выбирая случайные символы из списка characters
        password = ''.join(random.choice(characters) for in range(length))

        # Проверяем, содержит ли пароль хотя бы одну букву, цифру и специальный символ
        if any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in string.punctuation for char in password):
            return password


password = generate_password()
print("Сгенерированный пароль:", password)