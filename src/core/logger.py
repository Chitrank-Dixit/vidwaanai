"""Logging configuration."""

import logging
import sys
from src.core.config import settings

def get_logger(name: str) -> logging.Logger:
    """Get configured logger."""
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(settings.LOG_LEVEL)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(settings.LOG_LEVEL)

    return logger
