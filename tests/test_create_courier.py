import allure
from pages.page_api import ApiPage

class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier(self):
        ApiPage.test_create_courier(self)

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_was_created(self):
        ApiPage.test_courier_was_created(self)

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        ApiPage.test_create_courier_without_login(self)
    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        ApiPage.test_create_courier_without_password(self)