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

    @allure.title('успешный запрос возвращает объект с заказом')
    def test_success_get_order_return_order(self, authorize_courier, order):
        testgetorder = OrderMethods()
        responce = testgetorder.get_order_id(order[1]["track"])
        assert list(responce[1].keys()) == ['order']

    @allure.title('запрос без номера заказа возвращает ошибку')
    def test_get_order_out_number_order(self, authorize_courier, order):
        testgetorder = OrderMethods()
        responce = testgetorder.get_order_id()
        assert responce[0] == -1 and responce[1] == data.MSG_OUT_ARG

    @allure.title('запрос с несуществующим заказом возвращает ошибку')
    def test_success_get_not_success_number_order(self, authorize_courier, order):
        testgetorder = OrderMethods()
        responce = testgetorder.get_order_id(fake.random_int(1, 100))
        assert responce[0] == 404 and responce[1]["message"] == data.MSG_ORDER_NOT_FOUND
