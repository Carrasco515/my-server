# Mein Server
[![CI](https://github.com/Carrasco515/mein-server/actions/workflows/ci.yml/badge.svg)](https://github.com/Carrasco515/mein-server/actions/workflows/ci.yml)

This is my first practical DevOps learning project.

## Goal

The goal of this project is to learn how to build, containerize and run a small API with Docker and Docker Compose.

## Tech Stack

Python  
FastAPI  
Docker  
Docker Compose  
Git  
GitHub  

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Returns the main status message |
| GET | /health | Returns the health status of the application |
| GET | /docs | Opens the automatic FastAPI documentation |

## Run the project

```bash
docker compose up --build
## Run with Kubernetes

This project can also be deployed to a local Kubernetes cluster.

### Apply the Kubernetes manifests

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### Check the deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### Access the application with port forwarding

```bash
kubectl port-forward deployment/mein-server 8080:8000
```

Open the application in the browser:

```text
http://localhost:8080
```

Health check:

```text
http://localhost:8080/health
```

API documentation:

```text
http://localhost:8080/docs
```

### Stop port forwarding

Press:

```text
CTRL + C
```

## Kubernetes files

| File | Description |
|------|-------------|
| kubernetes/deployment.yaml | Defines the application deployment |
| kubernetes/service.yaml | Exposes the application inside Kubernetes |