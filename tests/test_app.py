from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_config_endpoint(monkeypatch):
    monkeypatch.setenv("APP_NAME", "My Server API")
    monkeypatch.setenv("APP_VERSION", "1.0.0")
    monkeypatch.setenv("APP_ENV", "test")

    response = client.get("/config")

    assert response.status_code == 200
    assert response.json() == {
        "app_name": "My Server API",
        "app_version": "1.0.0",
        "app_env": "test",
    }


def test_secret_status_endpoint(monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy-api-key")
    monkeypatch.setenv("DB_PASSWORD", "dummy-password")

    response = client.get("/secret-status")

    assert response.status_code == 200
    assert response.json() == {
        "api_key_loaded": True,
        "db_password_loaded": True,
    }