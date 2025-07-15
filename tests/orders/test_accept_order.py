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

# Можно через параметризацию, в задании не указано, поэтому отдельно каждый тест

    @allure.step('успешный запрос возвращает"ok":true')
    def test_success_accept_order_return_ok(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(int(responce[1]["order"]["id"]), int(authorize_courier[1]["id"]))
        assert responce[1] == {'ok': True}

    @allure.step('если не передать id курьера, запрос вернёт ошибку')
    def test_not_id_courier_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        try:
            responce = testacceptorder.accept_order(courier_id=int(responce[1]["order"]["id"]))
        except TypeError:
            responce = 'не передан обзательный аргумент'
        print(responce)
        assert responce == 'не передан обзательный аргумент'

    @allure.step('если передать неверный id курьера, запрос вернёт ошибку')
    def test_not_success_id_courier_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(int(responce[1]["order"]["id"]), fake.random_int(1, 100))
        print(responce[1]['message'])
        assert responce[1]['message'] == 'Курьера с таким id не существует'

    @allure.step('если не передать id заказа, запрос вернёт ошибк')
    def test_not_id_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        try:
            responce = testacceptorder.accept_order(id=int(responce[1]["order"]["id"]))
        except TypeError:
            responce = 'не передан обзательный аргумент'
        # responce = testacceptorder.accept_order(507499, 566857)
        print(responce)
        assert responce == 'не передан обзательный аргумент'

    @allure.step('если передать неверный id заказа, запрос вернёт ошибку')
    def test_not_exist_id_order(self, authorize_courier, order):
        testacceptorder = OrderMethods()
        responce = testacceptorder.get_order_id(int(order[1]["track"]))
        responce = testacceptorder.accept_order(fake.random_int(1, 100), int(authorize_courier[1]["id"]))
        print(responce[1])
        assert responce[1]["message"] == 'Заказа с таким id не существует'




