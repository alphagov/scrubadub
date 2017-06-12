import re

from .base import RegexDetector
from ..filth import PassportFilth


class PassportDetector(RegexDetector):
    """
    Use regex to find passport numbers
    """
    filth_cls = PassportFilth
