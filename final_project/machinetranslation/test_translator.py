import unittest

from translator import english_to_french, french_to_english

class Testenglishtofrench(unittest.TestCase):
    """A dummy docstring."""
    def test1(self):
        """A dummy docstring."""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  \
            # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')  \
            # test when 'Hello' is given as input the output is not 'Bonjour'.

class Testfrenchtoenglish(unittest.TestCase):
    """A dummy docstring."""
    def test1(self):
        """A dummy docstring."""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  \
            # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')  \
            # test when 'Bonjour' is given as input the output is not 'Hello'.

if __name__ == '__main__':
    unittest.main()
