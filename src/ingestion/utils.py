import os

TRACKING_FILE = os.path.join(
    os.path.dirname(__file__), "../../data/processed_files.txt"
)


def is_processed(file_path: str) -> bool:
    """Check if file has already been processed."""
    if not os.path.exists(TRACKING_FILE):
        return False

    abs_path = os.path.abspath(file_path)
    with open(TRACKING_FILE, "r") as f:
        processed = f.read().splitlines()

    return abs_path in processed


def mark_processed(file_path: str):
    """Mark file as processed."""
    abs_path = os.path.abspath(file_path)

    # Ensure directory exists (though data/ should exist)
    os.makedirs(os.path.dirname(TRACKING_FILE), exist_ok=True)

    with open(TRACKING_FILE, "a") as f:
        f.write(f"{abs_path}\n")


def should_process(file_path: str, force: bool = False) -> bool:
    """Determine if we should process this file."""
    if force:
        return True
    return not is_processed(file_path)
