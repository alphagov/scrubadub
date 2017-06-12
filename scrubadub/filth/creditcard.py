import re

from .base import RegexFilth


class CreditCardFilth(RegexFilth):
    type = 'creditcard'

    # Regexes from:
    # http://www.regular-expressions.info/creditcard.html

    # Fake card numbers from:
    # https://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm

    regex = re.compile((
        "(?<=\s)"
        "(?:4[0-9]{12}(?:[0-9]{3})?"  		# Visa
        "|(?:5[1-5][0-9]{2}"          		# MasterCard
        "|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}"
        "|3[47][0-9]{13}"             		# American Express
        "|3(?:0[0-5]|[68][0-9])[0-9]{11}"   	# Diners Club
        "|6(?:011|5[0-9]{2})[0-9]{12}"      	# Discover
        "|(?:2131|1800|35\d{3})\d{11})"      	# JCB
    ), re.VERBOSE)
