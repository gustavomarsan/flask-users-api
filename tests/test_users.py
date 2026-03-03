import pytest
from app import create_app  
from unittest.mock import patch


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with patch("services.user_services.get_connection") as mock_db:
        mock_db.side_effect = Exception("DB should not be called in tests")

        with app.test_client() as client:
            yield client
    

def test_get_users(client):
    fake_users = [
        {"id": 1, "name": "Test", "email": "test@test.com"}
    ]

    with patch("routes.user_routes.get_all_users", return_value=fake_users):
        response = client.get("/api/users")

        assert response.status_code == 200
        assert response.get_json() == fake_users
    

def test_create_user_success(client):
    fake_user = {"id": 1, "name": "Test", "email": "test@test.com"}

    with patch("routes.user_routes.create_user", return_value=fake_user):
        response = client.post(
            "/api/users",
            json={"name": "Test", "email": "test@test.com"}
        )

        assert response.status_code == 201
        assert response.get_json() == fake_user

def test_create_user_invalid_email(client):
    response = client.post(
        "/api/users",
        json={"name": "Test", "email": "invalid-email"}
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid email format"

def test_create_user_duplicate(client):
    with patch("routes.user_routes.create_user", return_value="duplicate"):
        response = client.post(
            "/api/users",
            json={"name": "Test", "email": "test@test.com"}
        )

        assert response.status_code == 409
        assert response.get_json()["error"] == "Email already exists"


def test_update_user_not_found(client):
    with patch("routes.user_routes.update_user", return_value=None):
        response = client.put(
            "/api/users/99",
            json={"name": "Test", "email": "test@test.com"}
        )

        assert response.status_code == 404

def test_delete_user_success(client):
    with patch("routes.user_routes.delete_user", return_value=True):
        response = client.delete("/api/users/1")

        assert response.status_code == 200

def test_create_user_missing_name(client):
    response = client.post(
        "/api/users",
        json={"email": "test@test.com"}
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Name and email are required"

def test_create_user_missing_email(client):
    response = client.post(
        "/api/users",
        json={"name": "Test"}
    )

    assert response.status_code == 400

def test_create_user_empty_json(client):
    response = client.post(
        "/api/users",
        json={}
    )

    assert response.status_code == 400

def test_create_user_no_json(client):
    response = client.post("/api/users")

    assert response.status_code == 400

def test_create_user_empty_strings(client):
    response = client.post(
        "/api/users",
        json={"name": "", "email": ""}
    )

    assert response.status_code == 400

def test_create_user_wrong_type(client):
    response = client.post(
        "/api/users",
        json={"name": 123, "email": 456}
    )

    assert response.status_code == 400

def test_create_user_space_strings(client):
    response = client.post(
        "/api/users",
        json={"name": " ", "email": " "}
    )

    assert response.status_code == 400