import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test1e(self):
        self.assertEqual(english_to_french("Hello"), 'Bonjour')
        self.assertNotEqual(english_to_french("None"), '')

    def test1f(self):
        self.assertEqual(french_to_english("Bonjour"), 'Hello')
        self.assertNotEqual(french_to_english("None"), '')

if __name__ == "__main__":
    unittest.main()