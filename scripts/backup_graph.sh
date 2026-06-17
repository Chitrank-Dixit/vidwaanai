#!/bin/bash
set -e

BACKUP_ROOT="data/backups/graph"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="$BACKUP_ROOT/$TIMESTAMP"
NEO4J_SERVICE="neo4j"

echo "=== BACKUP GRAPH (NEO4J) ==="
echo "Creating backup in: $BACKUP_DIR"
mkdir -p "$BACKUP_DIR"

echo "Stopping Neo4j for safe dump..."
docker compose stop "$NEO4J_SERVICE"

# Run a temporary container to dump
# Using --overwrite-destination as requested
echo "Running neo4j-admin dump..."
docker compose run --rm --entrypoint "" -v "$(pwd)/$BACKUP_DIR:/backups" "$NEO4J_SERVICE" neo4j-admin database dump neo4j --to-path=/backups --overwrite-destination

echo "Restarting Neo4j..."
docker compose start "$NEO4J_SERVICE"
echo "✓ Neo4j dump saved."

# Compress
tar -czf "$BACKUP_DIR.tar.gz" -C "$BACKUP_ROOT" "$TIMESTAMP"
rm -rf "$BACKUP_DIR"

echo "✅ Graph Backup Complete: $BACKUP_DIR.tar.gz"
