FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Avoid creating .pyc files and enable buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application source
COPY . /app

# Create a non-root user
RUN useradd --create-home appuser || true
USER appuser

EXPOSE 8080

ENV PORT=8080

# Run the app
CMD ["python", "app/main.py"]
