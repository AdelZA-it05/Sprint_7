import data
from conftest import courier
from conftest import authorize_courier
from faker import Faker
import json
import allure

fake = Faker()

from methods.cuorier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('проверка ручек авторизации курьера')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.title('курьер может авторизоваться')
    def test_courier_can_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(*courier[2])
        assert responce[0] == 200 and list(responce[1].keys()) == ['id']

    @allure.title('для авторизации нужно передать все обязательные поля')
    def test_empty_mandatory_param_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(*courier[2], is_param=2)
        assert responce[0] == 400 and responce[1]["message"] == data.MSG_OUT_DATA_FOR_LOGIN

    @allure.step('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_input_incorrect_param_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(courier[2][0], fake.password())
        assert responce[0] == 404 and responce[1]["message"] == data.MSG_UZ_NOT_FOUND

    @allure.title('если какого-то поля нет, запрос возвращает ошибку')
    def test_out_param_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(courier[2][0])
        assert responce[0] == 504

    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_input_fake_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(fake.user_name(), courier[2][1])
        assert responce[0] == 404 and responce[1]["message"] == data.MSG_UZ_NOT_FOUND

    @allure.step('успешный запрос возвращает id')
    def test_correct_login_return_id(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(*courier[2])
        assert responce[0] == 200 and list(responce[1].keys()) == ['id']
