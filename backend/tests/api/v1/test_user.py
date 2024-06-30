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
            'name': 'user',
            'email': 'user@example.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'name': 'user', 'email': 'user@example.com'}
    global created_user_email
    created_user_email = response.json().get('email')


def test_delete_user(client):
    assert created_user_email is not None
    response = client.delete(f'/users/{created_user_email}/')
    assert response.status_code == HTTPStatus.NO_CONTENT
    response = client.get(f'/users/{created_user_email}/')
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
