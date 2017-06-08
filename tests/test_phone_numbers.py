import unittest

from base import BaseTestCase


class PhoneNumberTestCase(unittest.TestCase, BaseTestCase):

    def create_docstring(self, phone_number):
        return """
        BEFORE: My phone number is %s
        AFTER:  My phone number is {{PHONE}}
        """ % phone_number

    def check_phone_numbers(self, *phone_numbers):
        for phone_number in phone_numbers:
            self.compare_before_after(
                docstring=self.create_docstring(phone_number),
            )

    def test_american_phone_number(self):
        """test GB-style phone numbers"""
        self.check_phone_numbers(
            '02079461234',
            '0207 946 1234',
            '+442079461234',
            '07912345678',
            '+447912345678',
            '08081 570123',
            '0909 8790123',
            '(03069) 990123',
            '03069 990123',
        )

    def test_extension_phone_numbers(self):
        """test phone numbers with extensions"""
        self.check_phone_numbers(
            '0207-946-1234 x12',
            '0207-946-1234 ext. 12',
            '0207-946-1234 ext.12',
        )

    def test_international_phone_numbers(self):
        """test international phone numbers"""
        self.check_phone_numbers(
            '+47 21 30 85 99',
            '+45 69 19 88 56',
            '+46 852 503 499',
            '+31 619 837 236',
            '+86 135 3727 4136',
            '+61267881324',
        )

    def test_multiple_phone_numbers(self):
        # running this through scrubadub.clean replaces 'reached at
        # 312.714.8142' with '{{EMAIL}}'. See issue
        result = self.clean(
            u'Call me on my cell 07912345678 or in my office 02079461234'
        )
        self.assertEqual(
            result,
            u'Call me on my cell {{PHONE}} or in my office {{PHONE}}',
            'problem with multiple phone numbers: \n %s' % result,
        )
