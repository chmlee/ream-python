#!/usr/bin/env python3
"""
REAM: REAM Ain't Markdown
~~~~~~~~~~~~~~~~~~~~~~~~~

This file is part of the ream package

:copyright: Copyright 2020 by Chih-Ming Louis Lee
:license: MIT, see LICENSE for details

"""

from . import convert
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='REAM decoder and encoder')
    parser.add_argument('--input', '-i', help='your input file')
    parser.add_argument('--output', '-o', help='output file, with extension')
    arg = parser.parse_args()
    #convert.convert(arg.input, arg.output)
    print(arg.input, arg.output)



