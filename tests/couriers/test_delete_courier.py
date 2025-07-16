import allure
from faker import Faker

import data

fake = Faker()


from conftest import courier
from conftest import authorize_courier
from methods.cuorier_methods import CourierMethods

class TestDeleteCourier:

    @allure.title('проверка ручек удаления курьера')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.title('неуспешный запрос возвращает соответствующую ошибку')
    @allure.title('если отправить запрос с несуществующим id, вернётся ошибка')
    def test_delete_fake_courier(self):
        testdeletecourier = CourierMethods()
        responce = testdeletecourier.delete_courier(fake.random_int(1, 100))
        assert responce[0] == 404 and responce[1]["message"] == data.MSG_OUT_COURIER_THIS_ID

    @allure.title('успешный запрос возвращает "ok":true')
    def test_delete_exist_courier(self):
        testdeletecourier = CourierMethods()
        courier_for_delete = testdeletecourier.create_courier()
        id_courier = testdeletecourier.login_courier(courier_for_delete[2][0], courier_for_delete[2][1])
        responce = testdeletecourier.delete_courier(id_courier[1]["id"])
        assert responce[1]== data.MSG_OK_CREATE

    @allure.title('если отправить запрос без id, вернётся ошибка')
    def test_delete_out_id_courier(self):
        testdeletecourier = CourierMethods()
        responce = testdeletecourier.delete_courier()
        assert responce[0] == -1 and responce[1] == data.MSG_OUT_ARG


