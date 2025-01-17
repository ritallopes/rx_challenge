from http import HTTPStatus


def test_main(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Bem-vindo!'}


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK


CREATED_EMAIL = 'user@example.com'


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'name': 'user',
            'email': CREATED_EMAIL,
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'name': 'user', 'email': CREATED_EMAIL}


def test_delete_user(client):
    assert CREATED_EMAIL is not None
    response = client.delete(f'/users/{CREATED_EMAIL}/')
    assert response.status_code == HTTPStatus.NO_CONTENT
    response = client.get(f'/users/{CREATED_EMAIL}/')
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
