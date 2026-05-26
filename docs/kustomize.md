# Kustomize

## Goal

This document explains how this project uses Kustomize to manage Kubernetes manifests for different environments.

## Structure

```text
kubernetes
  base
    deployment.yaml
    service.yaml
    kustomization.yaml

  overlays
    dev
      namespace.yaml
      configmap.yaml
      secret.yaml
      kustomization.yaml

## Production overlay

The project also includes a production overlay.

```text
kubernetes/overlays/prod