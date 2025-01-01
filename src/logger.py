import logging
import sys
from typing import Optional, TextIO


def setup_logger(
    name: str = "EAC",
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    stream: TextIO = sys.stderr,
) -> logging.Logger:
    """
    Set up a logger with a specific name, level, and output handlers.

    Parameters:
        name (str): Name of the logger (default: 'EAC').
        log_file (Optional[str]): File path for logging to a file. If None, only stream logging is used.
        level (int): Logging level (default: logging.INFO).
        stream (TextIO): Stream for logging (default: sys.stderr).

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        # Formatter for the log messages
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Stream handler (e.g., console)
        stream_handler = logging.StreamHandler(stream)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # File handler (if specified)
        if log_file is not None:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        # Set the logging level
        logger.setLevel(level)

    return logger
