#!/usr/bin/env python3
""" A basic script for logging """

import logging

logger = logging.getLogger(__name__)

def mylog():
    logging.info('Do someething')