import pytest, sys
from fastapi.testclient import TestClient
from pytest_bdd import scenarios, given, when, then, parsers
sys.path.append("..")
from routes.pedido import router
from config.database import pedido_table

scenarios("get_pedido.feature")

@pytest.fixture
def client():
    return TestClient(router)

def test_get_pedidos(client):
    response = client.get("/pedido/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@given("the pedido table has some data")
def populate_pedido_table(pedido_table):
    pass

@when("I request the list of pedidos")
def request_pedidos(client):
    response = client.get("/pedido/")
    return response

@then("the response status code should be 200")
def check_status_code(request_pedidos):
    assert request_pedidos.status_code == 200

@then("the response should contain a list of pedidos")
def check_response_content(request_pedidos):
    assert isinstance(request_pedidos.json(), list)
