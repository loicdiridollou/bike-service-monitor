"""Testing the different routes of the application"""
import pytest
import datetime
from application import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client


def test_landing(client):
    rv = client.get('/')
    assert {'message': 'healthy'} == rv.get_json()


def test_time(client):
    rv = client.get('/time')
    assert rv.status_code == 200
    assert isinstance(rv.get_json()['time'], str)


def test_times(client):
    rv = client.get('/times')
    assert rv.status_code == 200
    

def test_error404(client):
    rv = client.get('/timegcbrrs')
    assert rv.status_code == 404


def test_error400(client):
    rv = client.delete('/times/gcbrrs')
    assert rv.status_code == 400
