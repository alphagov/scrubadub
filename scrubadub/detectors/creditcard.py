import re

from .base import RegexDetector
from ..filth import CreditCardFilth


class CreditCardDetector(RegexDetector):
    """
    Use regex to find common Credit Card Numbers
    """
    filth_cls = CreditCardFilth
