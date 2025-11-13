FROM python:3.13-slim

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY load.py /app/load.py
RUN pip install --no-cache-dir psycopg2-binary
