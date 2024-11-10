#!/usr/bin/env python3
""" A python script that obfuscate a log message """

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ Returns an obfuscated log message """
    regex = fr"({'|'.join(fields)})={separator}*[^ {separator}]*"
    return re.sub(regex, lambda m: f"{m.group(1)}={redaction}", message)
