FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]