# Stop old containers if any
Write-Host "🛑 Stopping old containers..."
docker compose down

# Start containers detached (-d)
Write-Host "🔨 Starting containers in detached mode..."
docker compose up -d --build

# Wait for Postgres to be ready
Write-Host "⏳ Waiting for Postgres..."
do {
    Start-Sleep -Seconds 1
    $status = docker exec pg_dbt pg_isready -U dbt
} while ($status -notmatch "accepting connections")


Write-Host "✅ Containers started. dbt docs server should be started by the container's command."
Write-Host "View logs with: docker logs -f dbt"
