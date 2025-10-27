# Virus

## NiceGUI hello world

This repository now includes a minimal NiceGUI app at `app/main.py`.

Getting started:

```bash
# create virtual env (optional)
python3 -m venv .venv
source .venv/bin/activate

# install deps
pip install -r requirements.txt

# run the app
python app/main.py
```

Open http://localhost:8080 in your browser to see the app.

## Local development

Quick steps for running the app locally (recommended for contributors):

1. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app/main.py
```

By default the app listens on port 8080. To change the port set the `PORT` environment variable before running:

```bash
PORT=9000 python app/main.py
```

Quick verification (syntax check):

```bash
python -m py_compile app/main.py
```

Run with Docker locally (if you have Docker installed):

```bash
# build
docker build -t ghcr.io/butanding/virus:local .

# run (map port 8080)
docker run --rm -p 8080:8080 ghcr.io/butanding/virus:local
```

If you need to run Docker without sudo, add your user to the `docker` group and re-login:

```bash
sudo usermod -aG docker $USER
# then log out and log back in, or run 'newgrp docker' in the terminal
```

## Docker image and GitHub Container Registry (GHCR)

## Docker image and GitHub Container Registry (GHCR)

This repository includes a `Dockerfile` and a GitHub Actions workflow that builds and publishes a container image to GitHub Container Registry (GHCR) when you push to `main` or `hello_world`.

Image name (example):

```
ghcr.io/butanding/virus:latest
```

Build and publish locally (alternative to GitHub Actions):

```bash
# build
docker build -t ghcr.io/butanding/virus:latest .

# push (login first: `echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin`)
docker push ghcr.io/butanding/virus:latest
```

Deploy on your server:

```bash
# pull and run (replace tag if needed)
docker pull ghcr.io/butanding/virus:latest
docker run -d --name virus -p 8080:8080 ghcr.io/butanding/virus:latest
```

If you want GitHub Actions to push the image, no additional secrets are required; the `GITHUB_TOKEN` is used with appropriate workflow permissions.
