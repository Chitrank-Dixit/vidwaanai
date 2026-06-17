import os


def merge_files():
    source_dir = "ontology_project/queries/Ramayan"
    output_dir = "ontology_project/queries/Ramayan_Merged"
    os.makedirs(output_dir, exist_ok=True)

    # Define batches: (Batch ID, Start Index, End Index Inclusive, Agent)
    batches = [
        (1, 1, 16, "Gemini"),
        (2, 17, 32, "Gemini"),
        (3, 33, 48, "Gemini"),
        (4, 49, 64, "Gemini"),
        (5, 65, 80, "ChatGPT"),
        (6, 81, 96, "ChatGPT"),
        (7, 97, 112, "ChatGPT"),
        (8, 113, 128, "ChatGPT"),
        (9, 129, 144, "Perplexity"),
        (10, 145, 160, "Perplexity"),
        (11, 161, 176, "Perplexity"),
        (12, 177, 196, "Perplexity"),
    ]

    print(f"Merging files from {source_dir} to {output_dir}...")

    for batch_id, start_idx, end_idx, agent in batches:
        merged_content = f"# Merged Batch {batch_id} (Files {start_idx}-{end_idx})\n"
        merged_content += f"# Assigned Agent: {agent}\n\n"

        file_count = 0
        for i in range(start_idx, end_idx + 1):
            filename = f"Ramayan_batch_{i}.md"
            filepath = os.path.join(source_dir, filename)

            if os.path.exists(filepath):
                with open(filepath) as f:
                    content = f.read()
                    merged_content += f"\n\n--- Start of {filename} ---\n\n"
                    merged_content += content
                    merged_content += f"\n\n--- End of {filename} ---\n"
                file_count += 1
            else:
                print(f"Warning: File not found: {filepath}")

        output_filename = f"Batch_{batch_id}_{agent}.md"
        output_path = os.path.join(output_dir, output_filename)

        with open(output_path, "w") as f:
            f.write(merged_content)

        print(f"Created {output_filename}: {file_count} files merged.")


if __name__ == "__main__":
    merge_files()
