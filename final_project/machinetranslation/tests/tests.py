import unittest
from ..translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "")  # null input
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # Hello to Bonjour


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "")  # null input
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # Bonjour to Hello


if __name__ == '__main__':
    unittest.main()
