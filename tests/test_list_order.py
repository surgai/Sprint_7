import allure
import requests
from urls import Urls


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        CREATE_ORDER= '/api/v1/courier'
        response = requests.get(f'{Urls.URL}{CREATE_ORDER}')
        assert response.status_code == 200 and "orders" in response.json()