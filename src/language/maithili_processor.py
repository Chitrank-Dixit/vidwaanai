from src.dialects.maithili import MaithiliProcessor as NewMaithiliProcessor


class MaithiliProcessor(NewMaithiliProcessor):
    """
    Legacy wrapper for MaithiliProcessor.
    Now uses the robust implementation from src.dialects.maithili.
    """

    def __init__(self) -> None:
        super().__init__()
