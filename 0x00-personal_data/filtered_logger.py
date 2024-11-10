#!/bin//usr/env python3
""" A python script that obfuscate a log message """

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ Returns an obfuscated log message """
    return re.sub(
        fr"(?<=({separator})?({'|'.join(fields)})=)[^{separator}]*",
        redaction,
        message
    )
    