"""Testing the different routes of the application."""

import pytest

from application import create_app

# pylint: disable=W0621


@pytest.fixture
def client():
    """Define client fixture."""
    app = create_app({"TESTING": True})

    with app.test_client() as client_fixt:
        yield client_fixt


def test_landing(client):
    """Test landing page route."""
    request = client.get("/")
    assert {"message": "healthy"} == request.get_json()


def test_time(client):
    """Test time route."""
    request = client.get("/time")
    assert request.status_code == 200
    assert isinstance(request.get_json()["time"], str)


def test_times(client):
    """Test times route."""
    request = client.get("/times")
    assert request.status_code == 200


def test_error404(client):
    """Test error handler 404."""
    request = client.get("/timegcbrrs")
    assert request.status_code == 404


def test_error400(client):
    """Test error handler 400."""
    request = client.delete("/times/gcbrrs")
    assert request.status_code == 400
