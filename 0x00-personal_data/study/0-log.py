#!/usr/bin/env python3
""" script to test the basic logging """

import logging

# Setup logger config
logger = logging.getLogger(__name__)
logging.basicConfig(filename='abdc.log', encoding='utf-8', level=logging.DEBUG)

logger.debug('Log mess to log file')
logger.info('Also this')
logger.warning('and warnings to')
logger.error('Add non-AsCII chacters also')