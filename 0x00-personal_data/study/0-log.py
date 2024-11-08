#!/usr/bin/env python3
""" script to test the basic logging """

import logging

# Setup logger config
logger = logging.getLogger(__name__)
# encoding= available from python 3.9>. Threrfore i used handlers
handler = logging.FileHandler(filename='0-log.log', encoding='utf-8')
logging.basicConfig(level=logging.DEBUG, handlers=[handler])

logger.debug('Log mess to log file')
logger.info('Also this')
logger.warning('and warnings to')
logger.error('Add non-AsCII chacters also')