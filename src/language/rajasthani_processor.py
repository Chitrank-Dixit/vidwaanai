from src.dialects.rajasthani import RajasthaniProcessor as NewRajasthaniProcessor


class RajasthaniProcessor(NewRajasthaniProcessor):
    """
    Legacy wrapper for RajasthaniProcessor.
    Now uses the robust implementation from src.dialects.rajasthani.
    """

    def __init__(self) -> None:
        super().__init__()
