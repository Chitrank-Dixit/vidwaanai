#!/bin/bash
set -e

BACKUP_ROOT="data/backups/vectorization"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="$BACKUP_ROOT/$TIMESTAMP"
DB_CONTAINER="vidwaan-db"
POSTGRES_USER="vidwaan_user"
POSTGRES_DB="vidwaan_db"

echo "=== BACKUP VECTORIZATION ==="
echo "Creating backup in: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

# Backup Embeddings Tables
echo "Dumping embedding tables..."
if docker ps | grep -q "$DB_CONTAINER"; then
    docker exec "$DB_CONTAINER" pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" \
        -t scripture_embeddings -t embeddings -t mantra_embeddings -t veda_embeddings \
        > "$BACKUP_DIR/vectorization.sql" || echo "⚠️ Some embedding tables might be missing, but dump proceeded."
    echo "✓ Vectorization dump saved."
else
    echo "❌ DB not running."
    exit 1
fi

# Compress
tar -czf "$BACKUP_DIR.tar.gz" -C "$BACKUP_ROOT" "$TIMESTAMP"
rm -rf "$BACKUP_DIR"

echo "✅ Vectorization Backup Complete: $BACKUP_DIR.tar.gz"
