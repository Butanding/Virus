# Virus

A simple Hello World example application using the NiceGUI Python framework.

## About

This project demonstrates a basic web application built with [NiceGUI](https://nicegui.io/), a Python-based web framework for creating user interfaces.

## Features

- Simple "Hello World" web interface
- Interactive button with notifications
- Containerized with Docker
- Automated deployment to GitHub Container Registry (GHCR)

## Running Locally

### With Python

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:8080`

### With Docker

1. Build the Docker image:
```bash
docker build -t virus-nicegui .
```

2. Run the container:
```bash
docker run -p 8080:8080 virus-nicegui
```

3. Open your browser and navigate to `http://localhost:8080`

### From GHCR

Pull and run the pre-built image from GitHub Container Registry:
```bash
docker pull ghcr.io/butanding/virus:latest
docker run -p 8080:8080 ghcr.io/butanding/virus:latest
```

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow (`.github/workflows/docker-build-push.yml`) that automatically:
- Builds the Docker image on push to main/master branches
- Pushes the image to GitHub Container Registry (GHCR)
- Tags images appropriately based on branch, PR, or version tags
- Uses Docker layer caching for faster builds

## Project Structure

```
.
├── app.py                              # Main NiceGUI application
├── requirements.txt                     # Python dependencies
├── Dockerfile                          # Docker configuration
├── .github/
│   └── workflows/
│       └── docker-build-push.yml      # GitHub Actions workflow
└── README.md                          # This file
```