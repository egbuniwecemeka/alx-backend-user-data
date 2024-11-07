#!/usr/bin/env python3
""" Script to demonstrate basic logging with an external library"""

import logging
import mylib

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)

def main():
    logger.info('Starting')
    mylib.mylog()
    logger.info('Finished')


if __name__ == '__main__':
    main()