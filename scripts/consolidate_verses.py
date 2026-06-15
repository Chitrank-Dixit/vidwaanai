import os

QUERIES_DIR = "ontology_project/queries/Ramayan"
OUTPUT_FILE = "ontology_project/queries/Ramayan/consolidated_verses_171_196.txt"

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for batch_id in range(171, 197):
        filename = f"Ramayan_batch_{batch_id}.md"
        filepath = os.path.join(QUERIES_DIR, filename)
        if os.path.exists(filepath):
            out.write(f"\n================ BATCH {batch_id} ================\n")
            with open(filepath, encoding="utf-8") as f:
                lines = f.readlines()
                current_verse = ""
                in_verse = False
                for line in lines:
                    if line.startswith("### Verse"):
                        current_verse = line.strip()
                        out.write(f"\n{current_verse}\n")
                    elif line.strip().startswith(
                        "- **Original**:"
                    ) or line.strip().startswith("- **Translation**:"):
                        out.write(line)
        else:
            out.write(f"\nBatch {batch_id} not found.\n")

print(f"Consolidated verses saved to {OUTPUT_FILE}")
