
# aberdeen/utils/error_messages.py
#
"""
Utility functions which print errors in a nice form
"""

import sys

from termcolor2 import c

def warning(err, *args, outfile=sys.stderr):
    """
    Prints a warning error to 'outfile'. This message is automatically formatted
    """
    warn = c("warning:").yellow + " "
    print (warn + err.format(*args), file=outfile)

def error(err, *args, outfile=sys.stderr):
    """
    Prints an error to 'outfile'. Message is formatted automatically
    """
    fatal = c("Error:").red + " "
    print (fatal + err.format(*args), file=outfile)
