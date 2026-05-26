import os

from fastapi import FastAPI

app = FastAPI(
    title="Mein Server API",
    description="My first Dockerized FastAPI application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Mein Server läuft erfolgreich in Version 2!",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/config")
def get_config():
    return {
        "app_name": os.getenv("APP_NAME", "not set"),
        "app_version": os.getenv("APP_VERSION", "not set"),
        "app_env": os.getenv("APP_ENV", "not set")
    }


@app.get("/secret-status")
def secret_status():
    api_key = os.getenv("API_KEY")
    db_password = os.getenv("DB_PASSWORD")

    return {
        "api_key_loaded": api_key is not None,
        "db_password_loaded": db_password is not None
    }