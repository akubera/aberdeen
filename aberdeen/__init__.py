#!/usr/bin/env python3
#
# aberdeen
#
"""
A static file CMS generator
"""
__author__ = "Andrew Kubera"
__version__ = "0.0.0"
__license__ = "Apache 2.0"
__contact__ = 'andrew.kubera@gmail.com'
__homepage__ = 'https://github.com/akubera/aberdeen'

import json
import sys

from glob import glob

def main(args):
    """The 'main' function called when executing aberdeen"""
    from markdown import Markdown
    if len(args) == 0:
        print ("DEFAULT")


if __name__ == "__main__":
    main(sys.argv)
