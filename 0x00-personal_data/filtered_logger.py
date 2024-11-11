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

    def __init__(self, fields: List):
        """ Initializing """
        super(RedactingFormatter).__init__(self.FORMAT)
        self.fields = fields
    
    def format(self, record: logging.LogRecord) -> str:
        """Formays log records by redacting specified fields."""
        main_message = record.getMessage()
        redacted_message = filter_datum(self.fields, self.REDACTION, main_message, self.SEPARATOR)
        record.message = redacted_message
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns an obfuscated log message """
    regex = fr"({'|'.join(fields)})={separator}*[^ {separator}]*"
    return re.sub(regex, lambda m: f"{m.group(1)}={redaction}", message)
