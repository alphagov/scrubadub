import unittest

from base import BaseTestCase


class NinoTestCase(unittest.TestCase, BaseTestCase):
    """
    Test cases for National Insurance Number (NINO) removal. Also provides
    test cases for when nino and name detectors clash.
    """

    def test_nino(self):
        """
        BEFORE: My nino is AB121314C.
        AFTER:  My nino is {{NINO}}.
        """
        self.compare_before_after()

    def test_nino_with_spaces(self):
        """
        Note strange behaviour here, despite regex including 'B' in second
        character, it does not seem to be found by the regex, See next test

        BEFORE: My nino is AC 121314 C.
        AFTER:  My nino is {{NINO}}.
        """
        self.compare_before_after()

    def test_nino_name_clash(self):
        """
        Note strange behaviour here, despite regex including 'B' in second
        character, it does not seem to be found by the regex, See next test

        BEFORE: My nino is AB 121314 C.
        AFTER:  My nino is {{NINO+NAME}}.
        """
        self.compare_before_after()

    def test_disable_name(self):
        """
        BEFORE: My nino is AB 123456 C
        AFTER:  My nino is {{NINO}}
        """
        before, after = self.get_before_after()
        import scrubadub
        scrubber = scrubadub.Scrubber()
        scrubber.remove_detector('name')
        self.check_equal(after, scrubber.clean(before))

    def test_nino_missing_last_character(self):
        """
        BEFORE: My nino is AB121314.
        AFTER:  My nino is {{NINO}}.
        """
        self.compare_before_after()

