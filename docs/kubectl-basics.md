# kubectl Basics

## Check running pods

```bash
kubectl get pods
## Scale a deployment

Increase the application to two running pods:

```bash
kubectl scale deployment mein-server --replicas=2
## Resource requests and limits

Kubernetes can define how much CPU and memory an application should request and how much it is allowed to use.

Requests are the minimum resources the application asks for.

Limits are the maximum resources the application can use.

## Readiness probe

A readiness probe checks if the application is ready to receive traffic.

In this project the readiness probe checks:

```bash
/health
## ConfigMap

A ConfigMap is used to store configuration outside of the application code.

In this project the ConfigMap contains:

```bash
APP_ENV=kubernetes
APP_NAME=Mein Server API
APP_VERSION=1.0.0