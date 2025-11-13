#!/usr/bin/env python3
import os
import time
import psycopg2
from pathlib import Path

PGHOST = os.environ.get("PGHOST", "postgres")
PGPORT = os.environ.get("PGPORT", "5432")
PGUSER = os.environ.get("PGUSER", "dbt")
PGPASSWORD = os.environ.get("PGPASSWORD", "dbt")
PGDATABASE = os.environ.get("PGDATABASE", "dbt_demo")

CSV_DIR = Path("/data")
FILES = None  # will be auto-populated by scanning CSV_DIR


def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host=PGHOST, port=PGPORT, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE
            )
            conn.close()
            print("✅ Postgres is ready")
            break
        except Exception as e:
            print("⏳ Waiting for Postgres...", str(e))
            time.sleep(2)


def load_csv(filename):
    path = CSV_DIR / filename
    if not path.exists():
        print(f"⚠️  File not found: {path}")
        return

    table_name = path.stem
    conn = psycopg2.connect(
        host=PGHOST, port=PGPORT, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE
    )
    cur = conn.cursor()

    cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")

    # example schema, tweak columns as needed
    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS raw.{table_name} (
        date DATE,
        product TEXT,
        price NUMERIC,
        quantity INT
    );
    """)

    # truncate before reload for idempotency
    cur.execute(f"TRUNCATE TABLE raw.{table_name};")

    with open(path, "r", encoding="utf-8") as f:
        cur.copy_expert(
            f"COPY raw.{table_name}(date, product, price, quantity) FROM STDIN WITH CSV HEADER",
            f,
        )

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {filename} → raw.{table_name}")


def main():
    wait_for_postgres()
    
    # Auto-discover all CSV files in CSV_DIR
    csv_files = sorted(CSV_DIR.glob("*.csv"))
    if not csv_files:
        print(f"⚠️  No CSV files found in {CSV_DIR}")
        return
    
    print(f"📂 Found {len(csv_files)} CSV file(s): {[f.name for f in csv_files]}")
    
    for csv_path in csv_files:
        load_csv(csv_path.name)
    print("🎉 All CSVs loaded successfully.")


if __name__ == "__main__":
    main()
