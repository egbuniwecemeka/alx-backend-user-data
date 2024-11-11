#!/usr/bin/env python3
""" A python script that obfuscate a log message """

from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)s %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializing formatter with specific fields to redact"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats log records by redacting specified fields."""
        main_message = record.getMessage()
        redacted_message = filter_datum(self.fields, self.REDACTION,
                                        main_message, self.SEPARATOR)
        record.msg = redacted_message
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns an obfuscated log message """
    regex = fr"({'|'.join(fields)})=[^ {separator}]*"
    return re.sub(regex, lambda m: f"{m.group(1)}={redaction}", message)

def get_logger() -> logging.Logger:
    """Logs message up to .INFO severity level"""
    # Create logger named user_data
    logger = logging.getLogger("user_data")
    # Set level to INFO
    logger.setLevel(logging.INFO)
    # Do not propagate message to other loggers
    logger.propagate = False
    # Create a streamHandler for outputing to console
    stream_handler = logging.StreamHandler()
    # Create a RedactingFormatter
    formatter = RedactingFormatter(fields=["email", "ssn", "password"])
    # Set the formatter for the streamHandler
    stream_handler.setFormatter(formatter)
    # Add handler to the logger
    logger.addHandler(stream_handler)

    return logger
