import unittest

from base import BaseTestCase


class PassportTestCase(unittest.TestCase, BaseTestCase):
    """
    Test cases for Credit Card number removal removal.
    """

    def test_passport_long(self):
        """
        Expect clash with NINO

        BEFORE: My passport number is 5333800068GBR8812049F2509286.
        AFTER:  My passport number is {{PASSPORT+NINO}}.
        """
        self.compare_before_after()

    def test_passport_short(self):
        """
        BEFORE: My passport number is 5333800068.
        AFTER:  My passport number is {{PASSPORT}}.
        """
        self.compare_before_after()

    def test_disable_name(self):
        """
        BEFORE: My passport number is 5333800068GBR8812049F2509286.
        AFTER:  My passport number is {{PASSPORT}}.
        """
        before, after = self.get_before_after()
        import scrubadub
        scrubber = scrubadub.Scrubber()
        scrubber.remove_detector('nino')
        self.check_equal(after, scrubber.clean(before))

