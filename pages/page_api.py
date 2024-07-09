
import requests
from urls import Urls
from generation import register_new_courier_and_return_login_password as gen
from generation import register_new_courier_without_login as gen_without_login
from generation import register_new_courier_without_login as gen_without_password
from constanta import Handle



class ApiPage:
    data = gen()

    def test_create_courier(self):
        return requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', ApiPage.data)

    def test_courier_was_created(self):
        return requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', ApiPage.data)

    def test_create_courier_without_login(self):
        return requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', gen_without_login())

    def test_create_courier_without_password(self):
        return requests.post(f'{Urls.URL}{Handle.CREATE_COURIER}', gen_without_password())
