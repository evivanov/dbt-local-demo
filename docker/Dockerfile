FROM python:3.13-slim

# Install dbt + Postgres adapter
RUN pip install --no-cache-dir dbt-core dbt-postgres

# Utilities for scripts and file watching
RUN apt-get update && apt-get install -y nano git && rm -rf /var/lib/apt/lists/*

WORKDIR /dbt
