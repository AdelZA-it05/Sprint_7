import requests
import string
import random
import json
import allure
import data

class CourierMethods():

    @allure.step('получение рандомной строки (используется для создание курьера)')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('создание курьера')
    def create_courier(self, login=None, password=None, first_name=None, is_param=0):
        if is_param == 0:
            if not login: login = self.generate_random_string(10)
            if not password: password = self.generate_random_string(10)
            if not first_name: first_name = self.generate_random_string(10)
        elif is_param == 1:
            login = None
            if not password: password = self.generate_random_string(10)
            if not first_name: first_name = self.generate_random_string(10)
        elif is_param == 2:
            if not login: login = self.generate_random_string(10)
            password = None
            if not first_name: first_name = self.generate_random_string(10)
        elif is_param == 3:
            if not login: login = self.generate_random_string(10)
            if not password: password = self.generate_random_string(10)
            first_name = None
        courier_data = [login, password]

        response = requests.post(f'{data.BASE_URL}{data.COURIER_URL}', data={
            "login": login,
            "password": password,
})
        try:
            return response.status_code, response.json(), courier_data
        except Exception:
            return response.status_code, response.text, courier_data

    @allure.step('авторизацияя курьера')
    def login_courier(self, login=None, password=None, is_param=0):
        if is_param == 0:
            data_param = {
                "login": login,
                "password": password
            }
        elif is_param == 1:
            data_param = {
                "login": '',
                "password": password
            }
        elif is_param == 2:
            data_param = {
                "login": login,
                "password": ''
            }
        response = requests.post(f'{data.BASE_URL}{data.AUTORIZE_URL}', data=data_param)
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text


    @allure.step('удаление курьера')
    def delete_courier(self, id=None):
        if not id: return -1, data.MSG_OUT_ARG
        data_param = json.dumps({"id": str(id)})
        response = requests.delete(f'{data.BASE_URL}{data.DELETE_URL}{id}', data=data_param)
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text



