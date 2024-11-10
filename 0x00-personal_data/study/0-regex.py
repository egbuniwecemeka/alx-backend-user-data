#!/usr/bin/env python3
""" A python script to match basic regex patterns """

import re

text_to_search = '''
Hello123!
How_are you today?
(A-Z) [0-9]...
Testing! 42 degrees? $100.
'''

pattern = re.compile('\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
