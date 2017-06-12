import unittest

from base import BaseTestCase


class PhoneNumberTestCase(unittest.TestCase, BaseTestCase):
    """
    Numbers with 10 consecutive digits will clash with passport numbers.
    """
     
    def test_GB_phone_number(self):
        """
        BEFORE: My phone number is 02079461234.
        AFTER:  My phone number is {{PHONE+PASSPORT}}.
        """
        self.compare_before_after()

    def test_GB_phone_number(self):
        """
        BEFORE: My phone number is 0207 946 1234.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()
 
    def test_GB_phone_number_with_int_code(self):
        """
        BEFORE: My phone number is +442079461234.
        AFTER:  My phone number is {{PHONE+PASSPORT}}.
        """
        self.compare_before_after()
    
    def test_GB_mobile_number(self):
        """
        BEFORE: My phone number is 07912345678.
        AFTER:  My phone number is {{PHONE+PASSPORT}}.
        """
        self.compare_before_after()
        
    def test_GB_mobile_number_with_int_code(self):
        """
        BEFORE: My phone number is +447912345678.
        AFTER:  My phone number is {{PHONE+PASSPORT}}.
        """
        self.compare_before_after()

    def test_GB_phone_number_with_space(self):
        """
        BEFORE: My phone number is 08081 570123.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_GB_phone_number_with_space2(self):
        """
        BEFORE: My phone number is 0909 8790123.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()
            
    def test_GB_phone_number_with_brackets(self):
        """
        BEFORE: My phone number is (03069) 990123.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()
            
    def test_GB_phone_number_with_space3(self):
        """
        BEFORE: My phone number is 03069 990123.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_extension_phone_number1(self):
        """
        BEFORE: My phone number is 0207-946-1234 x12.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()
    
    def test_extension_phone_number2(self):
        """
        BEFORE: My phone number is 0207-946-1234 ext. 12.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_extension_phone_number3(self):
        """
        BEFORE: My phone number is 0207-946-1234 ext.12.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()
        
    def test_international_phone_number1(self):
        """
        BEFORE: My phone number is +47 21 30 85 99.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_international_phone_number2(self):
        """
        BEFORE: My phone number is +45 69 19 88 56.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_international_phone_number3(self):
        """
        BEFORE: My phone number is +46 852 503 499.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_international_phone_number4(self):
        """
        BEFORE: My phone number is +31 619 837 236.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()
        
    def test_international_phone_number5(self):
        """
        BEFORE: My phone number is +86 135 3727 4136.
        AFTER:  My phone number is {{PHONE}}.
        """
        self.compare_before_after()

    def test_international_phone_number6(self):
        """
        BEFORE: My phone number is +61267881324.
        AFTER:  My phone number is {{PHONE+PASSPORT}}.
        """
        self.compare_before_after()

    def test_multiple_phone_numbers(self):
        # running this through scrubadub.clean replaces 'reached at
        # 312.714.8142' with '{{EMAIL}}'. See issue
        result = self.clean(
            u'Call me on my cell 07912345678 or in my office 02079461234'
        )
        self.assertEqual(
            result,
            u'Call me on my cell {{PHONE+PASSPORT}} or in my office {{PHONE+PASSPORT}}',
            'problem with multiple phone numbers: \n %s' % result,
        )
