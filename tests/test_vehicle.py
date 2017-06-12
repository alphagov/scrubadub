import unittest

from base import BaseTestCase


class NinoTestCase(unittest.TestCase, BaseTestCase):
    """
    Test cases for Vehicle registration Plates (VEHICLE) removal.
    """

    def test_vehicle(self):
        """
        BEFORE: My number plate is AB12ABC.
        AFTER:  My number plate is {{VEHICLE}}.
        """
        self.compare_before_after()

    def test_vehicle_with_lowercase(self):
        """
        BEFORE: My number plate is ab12abc.
        AFTER:  My number plate is {{VEHICLE}}.
        """
        self.compare_before_after()

    def test_vehicle_with_spaces(self):
        """
        Note there is a clash here with the NAME detector.

        BEFORE: My number plate is AB12 ABC.
        AFTER:  My number plate is {{VEHICLE+NAME}}.
        """
        self.compare_before_after()

    def test_vehicle_disable_name(self):
        """
        BEFORE: My number plate is AB12 ABC.
        AFTER:  My number plate is {{VEHICLE}}.
        """
        before, after = self.get_before_after()
        import scrubadub
        scrubber = scrubadub.Scrubber()
        scrubber.remove_detector('name')
        self.check_equal(after, scrubber.clean(before))
