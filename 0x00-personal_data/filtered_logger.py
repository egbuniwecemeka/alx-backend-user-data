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
        super(RedactingFormatter).__init__(self.FORMAT)
        self.fields = fields
    
    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Returns an obfuscated log message """
    regex = fr"({'|'.join(fields)})={separator}*[^ {separator}]*"
    return re.sub(regex, lambda m: f"{m.group(1)}={redaction}", message)
