import requests
import data
import json
import allure

from faker import Faker
fake = Faker()


class OrderMethods():

    @allure.step('создание заказа')
    def create_order(self, firstName=fake.first_name(), lastName=fake.last_name(), address=fake.address(), metrostation=fake.text(), phone=fake.phone_number(), rentTime = fake.random_int(1, 5), deliveryDate=fake.date(), comment=fake.text(), color=list("BLACK")):
        response = requests.post(f'{data.BASE_URL}{data.ORDER_URL}', data={
    "firstName": firstName,
    "lastName": lastName,
    "address": address,
    "metroStation": metrostation,
    "phone": phone,
    "rentTime": rentTime,
    "deliveryDate": deliveryDate,
    "comment": comment,
    "color": color
})
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    @allure.step('получение спсика заказов')
    def get_list_orders(self):
        response = requests.get(f'{data.BASE_URL}{data.ORDER_URL}')
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    @allure.step('подтверждение заказа')
    def accept_order(self, id=None, courier_id=None):
        if not id: return -1, data.MSG_OUT_ARG
        if not courier_id: return -1, data.MSG_OUT_ARG
        response = requests.put(f'{data.BASE_URL}{data.ORDER_URL}{data.ORDER_ACCEPT_URL}{id}?courierId={courier_id}')
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    @allure.step('получение заказа по track_idа')
    def get_order_id(self, track_id=None):
        if not track_id: return -1, data.MSG_OUT_ARG
        response = requests.get(f'{data.BASE_URL}{data.ORDER_URL}{data.ORDER_TRUCK_URL}?t={track_id}')
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text



