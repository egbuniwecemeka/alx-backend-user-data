#!/usr/bin/python3
""" A python script logging date/time in messages """

import logging
import sys

try:
    loglevel = sys.argv[1]
except:
    raise IndexError('Provide a loglevel...DEBUG, INFO, ERROR etc')

numeric_log = getattr(logging, loglevel.upper(), None)

if not isinstance(numeric_log, int):
    raise ValueError('Invalid log number: %s' % loglevel)

logging.basicConfig(filename='date_time.log', format='%(asctime)s:%(message)s', level=numeric_log)
logger = logging.getLogger(__name__)
logger.warning('This is a warning message')
logger.error('This is a error message')
