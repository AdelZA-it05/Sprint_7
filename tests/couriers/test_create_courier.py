import allure
from faker import Faker
fake = Faker()


from conftest import courier
from methods.cuorier_methods import CourierMethods

class TestCreateCourier:

    @allure.title('проверка ручек создания курьера')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.step('создание курьера')
    def test_create_one_courier(self, courier):
        assert courier[0] == 201

    @allure.step('нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, courier):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(*courier[2])
        assert responce[0] == 409

    @allure.step('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_create_empty_param_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(is_param=3)
        assert responce[1] == {'ok': True}

    @allure.step('чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_create_empty_mandatory_param_courier(self):
        testcreatecourier = CourierMethods()
        courier = testcreatecourier.create_courier(is_param=2)
        assert courier[1] == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.step('запрос возвращает правильный код ответа')
    def test_create_true_code_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier()
        assert responce[0] == 201

    @allure.step('успешный запрос возвращает "ok"')
    def test_create_true_ok_courier(self, courier):
        print(courier[1])
        assert courier[1] == {"ok": True}

    @allure.step('если одного из полей нет, запрос возвращает ошибку')
    def test_create_none_param_courier(self):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(is_param=1)
        assert responce[0] == 400

    @allure.step('если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_duplicate_login_courier(self, courier):
        testcreatecourier = CourierMethods()
        responce = testcreatecourier.create_courier(courier[2][0], fake.password())
        assert responce[1] == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
