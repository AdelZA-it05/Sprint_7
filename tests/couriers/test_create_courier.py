import allure
from faker import Faker

import data

fake = Faker()


from conftest import courier
from methods.cuorier_methods import CourierMethods

class TestCreateCourier:

    @allure.title('проверка ручек создания курьера')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.step('создание курьера')
    @allure.step('запрос возвращает правильный код ответа')
    @allure.step('успешный запрос возвращает "ok"')
    def test_create_one_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier()
        assert responce[0] == 201 and responce[1] == data.MSG_OK_CREATE

    @allure.title('нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, courier):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(*courier[2])
        assert responce[0] == 409 and responce[1]["message"] == data.MSG_DUPLICATE_COURIER

    @allure.title('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_create_empty_param_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(is_param=3)
        assert responce[0] == 201 and responce[1] == data.MSG_OK_CREATE

    @allure.title('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_create_empty_mandatory_param_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(is_param=2)
        assert responce[1]["message"] == data.MSG_NO_DATA_FOR_CREATE

    @allure.title('если одного из полей нет, запрос возвращает ошибку')
    def test_create_none_param_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(is_param=1)
        assert responce[0] == 400 and responce[1]["message"] == data.MSG_NO_DATA_FOR_CREATE

    @allure.title('если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_duplicate_login_courier(self, courier):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(courier[2][0], fake.password())
        assert responce[0] == 409 and responce[1]["message"] == data.MSG_LOGIN_IS_USED
