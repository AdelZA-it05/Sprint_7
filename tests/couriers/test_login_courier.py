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
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.step('курьер может авторизоваться')
    def test_courier_can_login(self, authorize_courier):
        assert authorize_courier[0] == 200

    @allure.step('для авторизации нужно передать все обязательные поля')
    def test_empty_mandatory_param_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(*courier[2], is_param=2)
        assert responce[0] == 400

    @allure.step('система вернёт ошибку, если неправильно указать логин или пароль')
    def test_input_incorrect_param_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(courier[2][0], fake.password())
        assert responce[0] == 404

    @allure.step('если какого-то поля нет, запрос возвращает ошибку')
    def test_out_param_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(courier[2][0])
        assert responce[0] == 504

    @allure.step('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_input_fake_login(self, courier):
        testlogincourier = CourierMethods()
        responce = testlogincourier.login_courier(fake.user_name(), courier[2][1])
        assert responce[0] == 404

    @allure.step('успешный запрос возвращает id')
    def test_correct_login_return_id(self, authorize_courier):
        assert authorize_courier[0] == 200 and list(authorize_courier[1].keys()) == ['id']