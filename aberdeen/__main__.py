#!/usr/bin/env python
#
# aberdeen/__main__.py
#
"""
Use python
"""

import sys


def main(argv=None):
    """
    The 'main' function called when executing aberdeen
    """

    if argv is None:
        argv = sys.argv[1:]

    if len(argv) == 0:
        print("Aberdeen!!")
    else:
        pass

    return 0

if __name__ == "__main__":
    sys.exit(main())
