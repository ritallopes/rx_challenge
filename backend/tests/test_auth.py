from http import HTTPStatus

from jwt import decode

from app.auth import SECRET_KEY, create_token_access


def test_token_jwat():
    data = {'teste': 'teste'}
    token = create_token_access(data)

    decoded = decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['teste'] == data['teste']
    assert decoded['exp']


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in token
    assert 'token_type' in token


def test_jwt_invalid_token(client):
    response = client.delete('/users/1', headers={'Authorization': 'Bearer invalido'})

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'CREDENCIAIS INVÁLIDAS'}
