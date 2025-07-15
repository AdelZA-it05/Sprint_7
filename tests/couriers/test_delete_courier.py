import allure
from faker import Faker
fake = Faker()


from conftest import courier
from conftest import authorize_courier
from methods.cuorier_methods import CourierMethods

class TestDeleteCourier:

    @allure.title('проверка ручек удаления курьера')
    @allure.description('Проверка работы и вывода корректной информации')
    @allure.testcase('Тест-кейс из финального задания Sprtint_7')
    @allure.issue('Ссылка на баг', 'BUG-007')

    @allure.step('неуспешный запрос возвращает соответствующую ошибку')
    @allure.step('если отправить запрос с несуществующим id, вернётся ошибка')
    def test_delete_fake_courier(self):
        testdeletecourier = CourierMethods()
        responce = testdeletecourier.delete_courier(fake.random_int(1, 100))
        # print(responce)
        assert responce[0] == 404

    @allure.step('успешный запрос возвращает "ok":true')
    def test_delete_exist_courier(self):
        testdeletecourier = CourierMethods()
        courier_for_delete = testdeletecourier.create_courier()
        # print(courier_for_delete[2][0], courier_for_delete[2][1])
        id_courier = testdeletecourier.login_courier(courier_for_delete[2][0], courier_for_delete[2][1])
        # login_courier(courier[2][0], courier[2][1])[1]["id"]
        # print(id_courier)
        responce = testdeletecourier.delete_courier(id_courier[1]["id"])
        # responce = testdeletecourier.delete_courier(str(id_courier))
        print(responce)
        assert responce[1]== {'ok': True}

    @allure.step('если отправить запрос без id, вернётся ошибка')
    def test_delete_out_id_courier(self):
        testdeletecourier = CourierMethods()
        try:
            responce = testdeletecourier.delete_courier()
        except Exception:
            responce = 'не задан аргумент'
        # print(responce)
        assert responce == 'не задан аргумент'




