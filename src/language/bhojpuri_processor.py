from src.dialects.bhojpuri import BhojpuriProcessor as NewBhojpuriProcessor


class BhojpuriProcessor(NewBhojpuriProcessor):
    """
    Legacy wrapper for BhojpuriProcessor.
    Now uses the robust implementation from src.dialects.bhojpuri.
    """

    def __init__(self) -> None:
        super().__init__()
