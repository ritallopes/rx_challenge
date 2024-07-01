import pytest
from fastapi.testclient import TestClient

from app.api.db.models import User
from app.auth import read_hash_password
from app.main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def user(session):
    pwd = 'teste'
    user = User(
        name='User',
        email='user@test.com',
        password=read_hash_password(pwd),
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password(pwd)

    return user


@pytest.fixture()
def token(client, user):
    response = client.post(
        '/token',
        data={'email': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']
