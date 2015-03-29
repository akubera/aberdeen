#
# aberdeen/utils/prompt.py
#
"""
Utility functions which prompt the user for input.
"""

from distutils.util import strtobool
from .error_messages import warning

def get_user_bool(prompt, default=None):
    """
    Uses distutils 'strtobool' function to interpret a request from the user.
    @param default: if default is not None, an empty response returns default,
                    else the function repeats question until it can interpret
                    an answer as a boolean (yes/no, t/f, etc).
    @return boolean: User's answer or the default provided
    """
    while True:
        try:
            res = strtobool(input(prompt))
        except ValueError:
            if default is not None:
                return default
            continue
        return res

def prompt_user(name, default=None, do_strip=True):
    """
    Prompts the user for a value and returns the answer
    @param name str: The request asked to user, don't include a ':'
    @param default: if default is not None, an empty response returns this value
    @param do_strip: this function will automatically strip answers' whitespace
    @return string: User's answer or the default provided
    """
    request = name
    if default is not None:
        request += " [{}]".format(default)
    request += ": "
    res = input(request)
    if do_strip:
        res = res.strip()
    if not res:
        if default is None:
            warning("Empty string given with no defaults.")
        res = default
    return res
