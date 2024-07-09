import allure
import requests
import pytest
from urls import Urls
from data import Users
from constanta import Handle
from http import HTTPStatus


class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self):
        response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', data=Users.data_current)
        print(response.text)
        assert response.status_code == HTTPStatus.OK.value and 'id' in response.text

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_courier_log_negative(self):
        response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', data=Users.data_negative)
        assert response.status_code == HTTPStatus.NOT_FOUND.value and 'Учетная запись не найдена' in response.text

    @pytest.mark.parametrize('data_without_login_or_password', [Users.data_without_login, Users.data_without_password])
    @allure.title('Ошибка при авторизации если не зполнить логин или пароль')
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}', data=data_without_login_or_password)
        assert response.status_code == HTTPStatus.BAD_REQUEST.value and 'Недостаточно данных для входа' in response.text