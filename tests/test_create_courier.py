import allure
from pages.page_api import ApiPage
from pages.page_api import gen
from http import HTTPStatus

class TestCreateCourier:
    data = gen()
    @allure.title('Создание курьера')
    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = ApiPage.test_create_courier(self)
        assert response.status_code == HTTPStatus.CREATED.value and response.text == response_body
    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self):
        response = ApiPage.test_courier_was_created(self)
        assert response.status_code == HTTPStatus.CONFLICT.value and 'Этот логин уже используется' in response.text
    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        response = ApiPage.test_create_courier_without_login(self)
        assert response.status_code == HTTPStatus.BAD_REQUEST.value and 'Недостаточно данных для создания учетной записи' in response.text
    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        response = ApiPage.test_create_courier_without_password(self)
        assert response.status_code == HTTPStatus.BAD_REQUEST.value and 'Недостаточно данных для создания учетной записи' in response.text
