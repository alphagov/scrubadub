import re

from .base import RegexFilth


class NinoFilth(RegexFilth):
    type = 'nino'

    # National Insurance Number Regex from:
    # https://stackoverflow.com/questions/10204378/regular-expression-to-validate-uk-national-insurance-number

    regex = re.compile((
        "(?!BG)(?!GB)(?!NK)(?!KN)(?!TN)(?!NT)(?!ZZ)"  # Disallowed combinations
        "(?:([A-CEGHJ-PR-TW-Z]|[a-ceghj-pr-tw-z])"    # First two digits
        "([A-CEGHJ-PR-TW-Z]|[a-ceghj-pr-tw-z]))"
        "(?:\s*\d\s*){6}(?:([A-D]|[a-d]))?"           # Digits and final char?
    ), re.VERBOSE)
