import allure
import requests
from urls import Urls
from constanta import Handle
from http import HTTPStatus

class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):

        response = requests.get(f'{Urls.URL}{Handle.LIST_ORDER}')
        print(response.text)
        assert response.status_code == HTTPStatus.OK.value and "orders" in response.json()