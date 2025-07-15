import pytest

from methods.cuorier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier():
    responce = CourierMethods().create_courier()
    yield responce
    CourierMethods.delete_courier(responce, CourierMethods.login_courier(responce, login=responce[2][0], password=responce[2][1])[1]['id'])


@pytest.fixture()
def authorize_courier(courier):
    responce = CourierMethods.login_courier(courier, login=courier[2][0], password=courier[2][1])
    return responce

@pytest.fixture()
def order():
    responce = OrderMethods().create_order()
    return responce

