import re

from .base import RegexDetector
from ..filth import NinoFilth


class NinoDetector(RegexDetector):
    """
    Use regex to find National Insurance Numbers (NINOs)
    """
    filth_cls = NinoFilth
