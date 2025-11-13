#!/bin/bash
set -e

# Install dependencies
echo "📦 Installing dbt dependencies..."
dbt deps

# Seed, models, tests, generate docs once
echo "🏗️ Initial run: seed, models, tests..."
dbt seed
dbt run
dbt test
dbt docs generate

# Start docs server once in background
echo "🌐 Starting dbt docs server on http://0.0.0.0:8080 ..."
dbt docs serve --host 0.0.0.0 --port 8080 &
DBT_SERVE_PID=$!

# Keep track of last modification time
LAST_MOD=0

# Watch models/ and data/ for changes or new files
echo "⏳ Watching models/ and data/ for changes..."
while true; do
    # Find latest modification timestamp among all files
    NEW_MOD=$(find models data -type f -printf "%T@\n" 2>/dev/null | sort -n | tail -1)
    
    # Compare with last known modification
    if [[ -z "$NEW_MOD" ]]; then
        sleep 10
        continue
    fi

    NEW_MOD_INT=${NEW_MOD%.*}
    if [[ "$NEW_MOD_INT" -gt "$LAST_MOD" ]]; then
        echo "🔄 Detected change or new file, regenerating docs..."
        dbt docs generate
        LAST_MOD=$NEW_MOD_INT
    fi

    sleep 10
done

# Cleanup on exit
trap "echo 'Stopping docs server...'; kill $DBT_SERVE_PID 2>/dev/null || true" EXIT
