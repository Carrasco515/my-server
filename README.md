# My Server

[![CI](https://github.com/Carrasco515/my-server/actions/workflows/ci.yml/badge.svg)](https://github.com/Carrasco515/my-server/actions/workflows/ci.yml)

This is my first Dockerized FastAPI learning project.

A small FastAPI application that I built to learn the fundamentals of containers, CI and Kubernetes step by step: first running it locally, then in Docker, then deploying it to a local Kubernetes cluster with Kustomize.

## Why this project exists

I wanted a simple, real application to practice the core DevOps workflow end to end:

- Write a small API
- Containerize it with Docker
- Test it automatically in CI
- Publish the image to a container registry
- Deploy it to Kubernetes with ConfigMaps, Secrets and Kustomize overlays

It is intentionally small. The goal was learning the tools, not building a production system.

## Tech Stack

- Python 3.12 / FastAPI / Uvicorn
- Docker & Docker Compose
- Pytest & Ruff (via GitHub Actions CI)
- GitHub Container Registry (GHCR)
- Kubernetes & Kustomize

## Features

- REST API with health check and config endpoints
- Dockerfile and Docker Compose setup with live reload for development
- CI pipeline that runs linting and tests on every push
- Automated image publishing to GHCR
- Kubernetes manifests with resource limits, readiness/liveness probes
- Kustomize base + dev/prod overlays with ConfigMaps and Secrets (dummy values only)

## Project Structure

```text
.
├── main.py                  # FastAPI application
├── tests/                   # Pytest tests
├── Dockerfile
├── docker-compose.yml
├── kubernetes/
│   ├── base/                # Deployment, Service, Kustomization
│   └── overlays/
│       ├── dev/             # Namespace, ConfigMap, Secret (dummy values)
│       └── prod/            # Same as dev + NodePort patch
├── docs/                    # My learning notes (kubectl, kustomize, CI, ...)
└── .github/workflows/       # CI and image publishing
```

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt

uvicorn main:app --reload
```

Run the tests:

```bash
pytest
```

## Docker Setup

```bash
docker compose up --build
```

The API is then available at `http://localhost:8000`.

A prebuilt image is also published to GHCR by the CI pipeline:

```bash
docker pull ghcr.io/carrasco515/my-server:latest
```

## Kubernetes Basics

The manifests use a Kustomize base with dev and prod overlays.

Deploy the dev overlay to a local cluster (e.g. minikube or kind):

```bash
kubectl apply -k kubernetes/overlays/dev
```

Check the deployment:

```bash
kubectl get pods -n my-server-dev
kubectl get services -n my-server-dev
```

Access the application with port forwarding:

```bash
kubectl port-forward deployment/my-server 8080:8000 -n my-server-dev
```

Then open `http://localhost:8080` in the browser. Stop port forwarding with `CTRL + C`.

Note: the Secret manifests only contain dummy values for learning purposes. Real secrets should never be committed to Git.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns the main status message |
| GET | `/health` | Health check (used by Kubernetes probes) |
| GET | `/config` | Shows configuration loaded from environment variables / ConfigMap |
| GET | `/secret-status` | Shows whether secrets were loaded (without exposing values) |
| GET | `/docs` | Automatic FastAPI documentation |

## What I Learned

- How to build and structure a small FastAPI application
- How Docker images and layers work, and why `.dockerignore` matters
- The difference between running with Docker Compose (dev, live reload) and a plain image
- How to write basic tests with pytest and run them in GitHub Actions
- How to publish container images to GHCR from CI
- Kubernetes basics: Deployments, Services, probes, resource limits
- How ConfigMaps and Secrets inject configuration into pods
- How Kustomize overlays separate dev and prod configuration

My notes on these topics are in the [`docs/`](docs/) folder.

## Roadmap

- [ ] Add an Ingress instead of NodePort
- [ ] Add a Helm chart version for comparison with Kustomize
- [ ] Try a rolling update with a real version change

## Portfolio Note

This project was my first step before building more advanced labs like KubeBase Platform and CloudBase Lab. It is kept simple on purpose — it documents where my DevOps learning path started.
