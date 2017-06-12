import re

from .base import RegexFilth


class VehicleFilth(RegexFilth):
    type = 'vehicle'

    # Vehicle Registration Plates from:
    # https://gist.github.com/harry-jones/755501192139820eeb65e030fe878f75
    # More cases available in above link, but can cause the regex to become
    # quire greedy. For now keep it simple!

    regex = re.compile((
        "([a-zA-Z]{2}[0-9]{2}(?:\s)?[a-zA-Z]{3})"  # Current system
        "|([a-zA-Z][0-9]{1,3}(?:\s)?[a-zA-Z]{3})"  # Old system
    ), re.VERBOSE)
