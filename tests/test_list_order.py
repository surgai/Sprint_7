import allure
import requests
from urls import Urls


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):
        LIST_ORDER = '/api/v1/orders?courierId=334509'
        response = requests.get(f'{Urls.URL}{LIST_ORDER}')
        print(response.text)
        assert response.status_code == 200 and "orders" in response.json()