# Kubernetes Rollouts

## Goal

This document explains how to deploy versioned Docker images with Kubernetes and how to roll back to a previous version.

## Current namespace

```bash
kubectl get all -n dev