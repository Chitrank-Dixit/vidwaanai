#!/usr/bin/env python3
"""clean_ontology_duplicates.py

Scan all ontology JSON files under `scripts/responses/gemini` and remove duplicate
entity definitions (e.g., "Ram" vs "Rama", case variations, trailing whitespace).
The script:
1. Creates a backup `<filename>.bak` for each JSON file.
2. Detects duplicate entity names using a case‑insensitive, whitespace‑stripped key.
3. Chooses a canonical entry (the first encountered) and merges attribute dicts.
4. Updates the `entities` list to contain only the canonical entry.
5. Rewrites any `relationships` that reference a duplicate name to the canonical name.
6. Writes a `duplicates_report.csv` summarising the changes.

Run with:
    python scripts/clean_ontology_duplicates.py
"""

import os
import json
import glob
import shutil
import csv
from collections import defaultdict

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "responses", "gemini")
)
REPORT_PATH = os.path.join(BASE_DIR, "duplicates_report.csv")

report_rows = []  # List of dicts for CSV

for json_path in glob.glob(os.path.join(BASE_DIR, "*.json")):
    # Create backup
    backup_path = json_path + ".bak"
    shutil.copy2(json_path, backup_path)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    entities = data.get("entities", [])
    relationships = data.get("relationships", [])

    # Map normalized name -> list of (index, entity)
    name_map = defaultdict(list)
    for idx, ent in enumerate(entities):
        norm = ent["name"].strip().lower()
        name_map[norm].append((idx, ent))

    # Track which indices to keep/delete
    indices_to_remove = set()
    name_replacements = {}  # old name -> canonical name

    for norm, occ in name_map.items():
        if len(occ) <= 1:
            continue  # no duplicates
        # Choose canonical entry – the first one in the list
        canon_idx, canon_ent = occ[0]
        canon_name = canon_ent["name"].strip()
        # Merge attributes from duplicates (later entries override earlier)
        merged_attrs = dict(canon_ent.get("attributes", {}))
        duplicate_names = []
        for dup_idx, dup_ent in occ[1:]:
            duplicate_names.append(dup_ent["name"])
            dup_attrs = dup_ent.get("attributes", {})
            merged_attrs.update(dup_attrs)
            indices_to_remove.add(dup_idx)
            name_replacements[dup_ent["name"].strip()] = canon_name
        # Update canonical entity attributes
        canon_ent["attributes"] = merged_attrs
        # Record report
        report_rows.append(
            {
                "original_names": ", ".join([e["name"].strip() for e in occ]),
                "canonical_name": canon_name,
                "duplicate_count": len(occ) - 1,
            }
        )

    # Remove duplicate entities (sorted descending to avoid index shift)
    if indices_to_remove:
        for idx in sorted(indices_to_remove, reverse=True):
            del entities[idx]

    # Update relationships to use canonical names
    for rel in relationships:
        for side in ("from", "to"):
            orig = rel.get(side)
            if orig is None:
                continue
            # Direct match
            if orig in name_replacements:
                rel[side] = name_replacements[orig]
            else:
                # Also handle case‑insensitive/whitespace‑insensitive matches
                norm = orig.strip().lower()
                if norm in name_map and len(name_map[norm]) > 1:
                    # Use the canonical name chosen earlier (first entry)
                    rel[side] = name_map[norm][0][1]["name"].strip()

    # Write cleaned JSON back (pretty‑print for readability)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Write CSV report
if report_rows:
    with open(REPORT_PATH, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["original_names", "canonical_name", "duplicate_count"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in report_rows:
            writer.writerow(row)
    print(f"Duplicate cleanup completed. Report saved to {REPORT_PATH}")
else:
    print("No duplicate entities found.")
