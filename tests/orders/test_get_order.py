import pytest
from faker import Faker
fake = Faker()
import allure

from conftest import order
from conftest import authorize_courier
from conftest import courier
from methods.order_methods import OrderMethods


class TestAcceptOrder:

    @allure.title('проверка ручек принятия заказа')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.step('успешный запрос возвращает объект с заказом')
    def test_success_get_order_return_order(self, authorize_courier, order):
        testgetorder = OrderMethods()
        responce = testgetorder.get_order_id(order[1]["track"])
        assert list(responce[1].keys()) == ['order']

    @allure.step('запрос без номера заказа возвращает ошибку')
    def test_get_order_out_number_order(self, authorize_courier, order):
        testgetorder = OrderMethods()
        try:
            responce = testgetorder.get_order_id()
        except TypeError:
            responce = 'не задан номер заказа'
        assert responce == 'не задан номер заказа'

    @allure.step('запрос с несуществующим заказом возвращает ошибку')
    def test_success_get_not_success_number_order(self, authorize_courier, order):
        testgetorder = OrderMethods()
        responce = testgetorder.get_order_id(fake.random_int(1, 100))
        assert responce[1]["message"] == 'Заказ не найден'
