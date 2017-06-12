import re

from .base import RegexFilth


class PassportFilth(RegexFilth):
    type = 'passport'

    # Passport regex adapted from:
    # http://regexlib.com/REDetails.aspx?regexp_id=2390

    regex = re.compile((
        "[0-9]{10}(?:((GBR)|(GBD)|(GBO)|(GBS)|(GBP)|(GBN))[0-9]{7}[U,M,F]{1}[0-9]{7,9})?"
    ), re.VERBOSE)
