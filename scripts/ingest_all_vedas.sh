#!/bin/bash
# scripts/ingest_all_vedas.sh

VEDAS=(
    "rig_ved:Rig Ved:rig"
    "yajur_ved:Yajur Ved:yajur"
    "sam_ved:Sama Ved:sam"
    "atharv_ved:Atharva Ved:atharv"
)

PDF_DIR="data/vedas"
mkdir -p "$PDF_DIR"

echo "Starting Veda Ingestion Batch Process..."

for veda_info in "${VEDAS[@]}"; do
    IFS=':' read -r filename name code <<< "$veda_info"
    
    pdf_path="$PDF_DIR/${filename}_hindi.pdf"
    
    if [ -f "$pdf_path" ]; then
        echo "------------------------------------------------"
        echo "Processing $name ($code) from $pdf_path..."
        uv run python scripts/ingest_vedas.py \
            --pdf "$pdf_path" \
            --ved "$name" \
            --code "$code"
        echo "✓ $name ingestion step completed."
    else
        echo "------------------------------------------------"
        echo "Wait: File not found: $pdf_path"
        echo "Please place the file '${filename}_hindi.pdf' in $PDF_DIR to ingest this Veda."
    fi
done

echo "------------------------------------------------"
echo "Batch processing finished."
