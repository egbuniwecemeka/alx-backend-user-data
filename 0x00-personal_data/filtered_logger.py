#!/bin//usr/env python
""" A python script that obfuscate a log message """

import logging
import re

# Creates a logger name after the module's name.
logger = logging.getLogger(__name__)
logging.basicConfig(filename='filter.log')


def filter_datum(fields: str, redaction: str, message: str, separator: str) -> str:
    """ Returns an obfuscated log message """