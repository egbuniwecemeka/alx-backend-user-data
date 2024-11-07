#!/usr/bin/env python3
""" Script to demonstrate basic logging with an external library"""

import logging
import mylib

# Logger setup
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Starting')
    mylib.mylog()
    logger.info('Finished')


if __name__ == '__main__':
    main()