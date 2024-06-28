from http import HTTPStatus

from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_get_root():
    client = TestClient(app) # Arrange

    response = client.get('/') #Act

    assert response.status_code == HTTPStatus.OK # Assert

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}
