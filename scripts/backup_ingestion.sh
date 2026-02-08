#!/bin/bash
set -e

BACKUP_ROOT="data/backups/ingestion"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="$BACKUP_ROOT/$TIMESTAMP"
DB_CONTAINER="vidwaan-db"
POSTGRES_USER="vidwaan_user"
POSTGRES_DB="vidwaan_db"

echo "=== BACKUP INGESTION ==="
echo "Creating backup in: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

# Backup State
if [ -f "data/processed_files.txt" ]; then
    cp "data/processed_files.txt" "$BACKUP_DIR/"
    echo "✓ processed_files.txt saved."
fi

# Backup DB Tables (Structure + Data)
# Including: scriptures, verses, vedas, mandalas, mantras, suktas (if any)
echo "Dumping ingestion tables..."
if docker ps | grep -q "$DB_CONTAINER"; then
    docker exec "$DB_CONTAINER" pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" \
        -t scriptures -t verses -t vedas -t mandalas -t mantras -t suktas \
        > "$BACKUP_DIR/ingestion_dump.sql" || echo "⚠️ Some tables might be missing, but dump proceeded."
    echo "✓ Ingestion dump saved."
else
    echo "❌ DB not running."
    exit 1
fi

# Compress
tar -czf "$BACKUP_DIR.tar.gz" -C "$BACKUP_ROOT" "$TIMESTAMP"
rm -rf "$BACKUP_DIR"

echo "✅ Ingestion Backup Complete: $BACKUP_DIR.tar.gz"
