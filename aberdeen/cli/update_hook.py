#!/usr/bin/env python3
#
# aberdeen/cli/update_hook.py
#
"""
This program prints the aberdeen update git-hook to standard output.
"""

import os
import sys
import aberdeen


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    aberdeen_path = os.path.dirname(aberdeen.__file__)
    update_filename = os.path.join(aberdeen_path, 'git_hooks', 'update')

    with open(update_filename, 'r') as update_hook:
        print(update_hook.read())

    return 0

if __name__ == "__main__":
    sys.exit(main())
