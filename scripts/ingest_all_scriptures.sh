#!/bin/bash
# Batch ingestion for extended scriptures

# Create output directory
mkdir -p output/logs
LOG_FILE="output/logs/ingest_scriptures.log"

echo "Starting Scripture Ingestion... (Logging to $LOG_FILE)" | tee -a "$LOG_FILE"



# Bhagavad Gita
if [ -f "data/bhagwat_geeta/bhagwat_geeta.pdf" ]; then
    echo "--------------------------------"
    echo "Ingesting Bhagavad Gita..."
    uv run python -u scripts/ingest_scripture.py --pdf "data/bhagwat_geeta/bhagwat_geeta.pdf" --name "Bhagavad Gita" --code "gita" --type "gita" 2>&1 | tee -a "$LOG_FILE"
else
    echo "Skipping Bhagavad Gita (data/bhagwat_geeta/bhagwat_geeta.pdf not found)"
fi

# Ramayana
if [ -f "data/ramayana/ramayana.pdf" ]; then
    echo "--------------------------------"
    echo "Ingesting Ramayana..."
    uv run python -u scripts/ingest_scripture.py --pdf "data/scriptures/ramayana.pdf" --name "Ramayana" --code "ram" --type "ramayana" 2>&1 | tee -a "$LOG_FILE"
else
    echo "Skipping Ramayana (data/ramayana/ramayana.pdf not found)"
fi

# Puranas (Ingest ALL files in data/puranas)
if [ -d "data/puranas" ]; then
    echo "--------------------------------"
    echo "Ingesting Puranas from data/puranas/ ..."
    
    for pdf_file in data/puranas/*.pdf; do
        if [ -f "$pdf_file" ]; then
            filename=$(basename -- "$pdf_file")
            filename_no_ext="${filename%.*}"
            
            # Generate readable name: replace - with space, title case (simple approximation)
            readable_name=$(echo "$filename_no_ext" | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1')
            
            # Generate code: lowercase, underscores
            code=$(echo "$filename_no_ext" | tr '-' '_' | tr '[:upper:]' '[:lower:]')
            
            echo "Processing: $readable_name ($filename)" | tee -a "$LOG_FILE"
            uv run python -u scripts/ingest_scripture.py --pdf "$pdf_file" --name "$readable_name" --code "$code" --type "purana" 2>&1 | tee -a "$LOG_FILE"
        fi
    done
else
    echo "Directory data/puranas not found."
fi

echo "--------------------------------"
echo "Batch Script Complete."
