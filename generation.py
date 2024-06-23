import json

import requests
import random
import string
from urls import Urls


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(12)
    password = generate_random_string(12)
    first_name = generate_random_string(10)

    # тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    payload_string = json.dumps(payload)
    # отправляем запрос на регистрацию курьера
    response = requests.post(f'{Urls.URL}/api/v1/courier', data=payload_string)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

def register_new_courier_without_login():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    login_pass = []
    # генерируем логин, пароль и имя курьера
    login = ''
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    payload_string = json.dumps(payload)
    # отправляем запрос на регистрацию курьера
    response = requests.post(f'{Urls.URL}/api/v1/courier', data=payload_string)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass


def register_new_courier_without_password():
    def register_new_courier_without_login():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login_pass = []
        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = ''
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        payload_string = json.dumps(payload)
        # отправляем запрос на регистрацию курьера
        response = requests.post(f'{Urls.URL}/api/v1/courier', data=payload_string)
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
        # возвращаем список
        return login_pass
