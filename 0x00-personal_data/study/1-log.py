#!/usr/bin/env python3
""" script error checking user input of the loglevel variable from the CLI """

import logging
import sys

# Capture loglevel as input from CLI
try:
    loglevel = sys.argv[1]
except:
    raise IndexError('Please provide a loglevel (DEBUG, INFO, ERROR)')

# Check validity of loglevel and get numeric level
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logging.basicConfig(level=numeric_level, filename='1-log.log', format='%(levelname)s:%(message)s')

logger = logging.getLogerr(__name__)
logger.debug('This is a debug message')
logger.info('This is am info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

