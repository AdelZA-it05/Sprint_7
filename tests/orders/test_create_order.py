import pytest
from faker import Faker
fake = Faker()
import allure

from conftest import order
from methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title('проверка ручек создания заказа')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.step('создание заказа')
    def test_create_orders(self, order):
        assert order[0] == 201

    @allure.step('проверка, что в теле ответа возвращается список заказов')
    def test_get_list_orders(self):
        testorders = OrderMethods()
        responce = testorders.get_list_orders()
        assert list(responce[1].keys())[0] == 'orders' and isinstance(responce[1]["orders"], list)

    @allure.step('Проверка, что, когда создаёшь заказ')
    @allure.step('можно указать один из цветов — BLACK или GREY')
    @allure.step('можно указать оба цвета')
    @allure.step('можно совсем не указывать цвет')
    @pytest.mark.parametrize('par_color', [[list("BLACK")], [list("GREY")],  [["BLACK", "GREY"]], list()])
    def test_create_orders_param(self, par_color):
        testorders = OrderMethods()
        responce = testorders.create_order(color=par_color)
        assert responce[0] == 201

    @allure.step('тело ответа содержит track')
    def test_track_in_responce_create_orders(self, order):
        assert list(order[1].keys()) == ['track']