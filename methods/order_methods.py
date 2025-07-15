import requests
import data
import json

from faker import Faker
fake = Faker()

from urllib.parse import quote_plus, unquote

class OrderMethods():

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

    def get_list_orders(self):
        response = requests.get(f'{data.BASE_URL}{data.ORDER_URL}')
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    def accept_order(self, id, courier_id):
        response = requests.put(f'{data.BASE_URL}{data.ORDER_URL}{data.ORDER_ACCEPT_URL}{id}?courierId={courier_id}')
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text

    def get_order_id(self, track_id):
        # print(f'{data.BASE_URL}{data.ORDER_URL}{data.ORDER_TRUCK_URL}')
        response = requests.get(f'{data.BASE_URL}{data.ORDER_URL}{data.ORDER_TRUCK_URL}?t={track_id}')
        # , data = {"t": track_id}
        # response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=653280')
        try:
            return response.status_code, response.json()
        except Exception:
            return response.status_code, response.text



