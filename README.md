# Virus

## NiceGUI hello world

<<<<<<< Updated upstream
This repository now includes a minimal NiceGUI app at `app/main.py`.
=======
This repository includes a minimal NiceGUI app at `app/main.py`.
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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
=======
# Virus

## NiceGUI hello world

This repository contains a minimal NiceGUI app located at `app/main.py`.

## Getting started

Create a virtual environment (recommended), install dependencies and run the app:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

Open http://localhost:8080 in your browser.

## Local development

Use a virtual environment and install the dependencies as shown above. Quick checks:

- Syntax check:
  ```bash
  python -m py_compile app/main.py
  ```
- Run on a different port:
  ```bash
  PORT=9000 python app/main.py
  ```

Run with Docker locally:

```bash
docker build -t ghcr.io/butanding/virus:local .
docker run --rm -p 8080:8080 ghcr.io/butanding/virus:local
```

If you prefer not to use `sudo` for Docker, add your user to the `docker` group and re-login:

```bash
sudo usermod -aG docker $USER
# then log out and log back in, or run: newgrp docker
>>>>>>> Stashed changes
```

## Docker image and GitHub Container Registry (GHCR)

<<<<<<< Updated upstream
## Docker image and GitHub Container Registry (GHCR)

This repository includes a `Dockerfile` and a GitHub Actions workflow that builds and publishes a container image to GitHub Container Registry (GHCR) when you push to `main` or `hello_world`.

Image name (example):
=======
This repository includes a `Dockerfile` and a GitHub Actions workflow that builds and publishes a container image to GitHub Container Registry (GHCR) when you push to `main` or `hello_world`.

Example image name:
>>>>>>> Stashed changes

```
ghcr.io/butanding/virus:latest
```

<<<<<<< Updated upstream
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
=======
Build and publish locally (alternative to CI):

```bash
docker build -t ghcr.io/butanding/virus:latest .
docker push ghcr.io/butanding/virus:latest
```

## Deployment

Overview: after a successful GitHub Actions run the image is available in GHCR. On your VPS (Dockge/Docker/Docker Compose) you pull the image and run or restart the container.

1) GitHub Actions (CI)
- The `docker-publish.yml` workflow builds and pushes the image to GHCR on push.

2) Server integration
- Use Docker or Docker Compose to run the image on the VPS. Example `docker-compose.yml` service:

```yaml
services:
  virus:
    image: ghcr.io/butanding/virus:latest
    environment:
      - PORT=8080
    ports:
      - "8080:8080"
    restart: unless-stopped
```

3) Authentication (private package)
- If the GHCR package is private, create a GitHub PAT with `read:packages` and login on the VPS:

```bash
echo $GHCR_PAT | docker login ghcr.io -u <github-username> --password-stdin
```

4) Force-update / refresh container
- Pull the new image and restart the container:

```bash
docker pull ghcr.io/butanding/virus:latest
docker stop virus || true
docker rm virus || true
docker run -d --name virus -e PORT=8080 -p 8080:8080 --restart unless-stopped ghcr.io/butanding/virus:latest
```

- Or with Docker Compose:

```bash
docker compose pull
docker compose up -d --no-deps --force-recreate
```

5) Automation options
- Add a small update script on the VPS (pull + recreate) and call it manually, via a systemd unit/timer, or from a GitHub Actions deploy job (SSH). Tools like Watchtower can also auto-update containers.

6) Production notes
- Prefer immutable tags (CI commit SHA) for production deployments.
- Add healthchecks and use a reverse proxy (nginx/Caddy) with TLS for public exposure.

If you want, I can add helper files (docker-compose.yml, an `update-virus.sh` script + systemd unit, and an optional GitHub Actions deploy job that SSHes to your VPS). Tell me which artifacts you want and I will add them.
>>>>>>> Stashed changes
