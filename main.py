from fastapi import FastAPI

app = FastAPI(
    title="Mein Server API",
    description="My first Dockerized FastAPI application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Mein Server läuft erfolgreich!",
        "status": "online"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }