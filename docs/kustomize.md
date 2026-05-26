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