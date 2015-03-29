#
# aberdeen/utils/prompt.py
#
"""
Utility functions which prompt the user for input.
"""

from distutils.util import strtobool


def get_user_bool(prompt, default=None):
    while True:
        try:
            res = strtobool(input(prompt))
        except ValueError:
            if default is not None:
                return default
            continue
        return res
