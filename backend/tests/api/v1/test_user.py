from datetime import datetime
from http import HTTPStatus


def test_main(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Bem-vindo!'}


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'john',
            'email': 'john@example.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'name': 'john', 'email': 'john@example.com'}
