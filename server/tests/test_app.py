from http import HTTPStatus

from app.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_root_must_return_ok():
    client.get('/').status_code == HTTPStatus.OK


def test_read_root_must_return_message():
    response = client.get('/')
    assert response.json() == {'message': 'Hello World!'}
