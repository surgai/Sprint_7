import allure
import requests
from urls import Urls
from generation import register_new_courier_and_return_login_password as gen
from generation import register_new_courier_without_login as gen_without_login
from generation import register_new_courier_without_login as gen_without_password


class TestCreateCourier:
    data = gen()

    @allure.title('Создание курьера')
    def test_create_courier(self):
        CREATE_COURIER = '/api/v1/courier'
        response_body = '{"ok":true}'
        response = requests.post(
            f'{Urls.URL}{CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 201 and response.text == response_body

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self):
        CREATE_COURIER = '/api/v1/courier'
        response = requests.post(
            f'{Urls.URL}{CREATE_COURIER}',
            TestCreateCourier.data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        CREATE_COURIER = '/api/v1/courier'
        response = requests.post(
            f'{Urls.URL}{CREATE_COURIER}',
            gen_without_login())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        CREATE_COURIER = '/api/v1/courier'
        response = requests.post(
            f'{Urls.URL}{CREATE_COURIER}',
            gen_without_password())
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text