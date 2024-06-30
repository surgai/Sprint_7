
import requests
from urls import Urls
from generation import register_new_courier_and_return_login_password as gen
from generation import register_new_courier_without_login as gen_without_login
from generation import register_new_courier_without_login as gen_without_password
from constanta import Handle
from http import HTTPStatus


class ApiPage:
    data = gen()


    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', ApiPage.data)
        assert response.status_code == HTTPStatus.CREATED.value and response.text == response_body


    def test_courier_was_created(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', ApiPage.data)
        assert response.status_code == HTTPStatus.CONFLICT.value and 'Этот логин уже используется' in response.text


    def test_create_courier_without_login(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', gen_without_login())
        assert response.status_code == HTTPStatus.BAD_REQUEST.value and 'Недостаточно данных для создания учетной записи' in response.text


    def test_create_courier_without_password(self):
        response = requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', gen_without_password())
        assert response.status_code == HTTPStatus.BAD_REQUEST.value and 'Недостаточно данных для создания учетной записи' in response.text