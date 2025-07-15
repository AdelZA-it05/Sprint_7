import pytest
from faker import Faker

import data

fake = Faker()
import allure

from conftest import order
from conftest import authorize_courier
from conftest import courier
from methods.order_methods import OrderMethods


class TestAcceptOrder:

    @allure.title('проверка ручек принятия заказа')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

# Можно через параметризацию, в задании не указано, поэтому отдельно каждый тест

    @allure.title('успешный запрос возвращает"ok":true')
    def test_success_accept_order_return_ok(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(int(responce[1]["order"]["id"]), int(authorize_courier[1]["id"]))
        assert responce[1] == data.MSG_OK_CREATE

    @allure.title('если не передать id курьера, запрос вернёт ошибку')
    def test_not_id_courier_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(courier_id=int(responce[1]["order"]["id"]))
        assert responce[0] == -1 and responce[1] == data.MSG_OUT_ARG

    @allure.title('если передать неверный id курьера, запрос вернёт ошибку')
    def test_not_success_id_courier_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(int(responce[1]["order"]["id"]), fake.random_int(1, 100))
        assert responce[0] == 404 and responce[1]['message'] == data.MSG_NOT_EXIST_COURIER_THIS_ID

    @allure.title('если не передать id заказа, запрос вернёт ошибк')
    def test_not_id_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(id=int(responce[1]["order"]["id"]))
        assert responce[0] == -1 and responce[1] == data.MSG_OUT_ARG

    @allure.step('если передать неверный id заказа, запрос вернёт ошибку')
    def test_not_exist_id_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(fake.random_int(1, 100), int(authorize_courier[1]["id"]))
        assert responce[0] and responce[1]["message"] == data.MSG_OUT_ORDER_THIS_ID
