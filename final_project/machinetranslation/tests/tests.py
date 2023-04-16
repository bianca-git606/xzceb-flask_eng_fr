from translator import english_to_french, french_to_english
import unittest

class TestTranslator(unittest.TestCase):

    def test_englishToFrench_for_null(self):
        '''
        this function tests the englishToFrench function with null values, and common eng-french translation
        '''
        self.assertEqual(english_to_french(' '), ' ')
    
    def test_englishToFrench_for_translation(self):
        '''
        this function tests the englishToFrench function for common eng-french translation
        '''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')


    def test_frenchToEnglish(self):
        '''
        this function tests the frenchToEnglish function with null values
        '''
        self.assertEqual(french_to_english(' '), ' ')

    def test_frenchTOEnglish_for_translation(self):
        '''
        this function tests the frenchToEnglish function for common french-eng translation
        '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        

if __name__ == '__main__':
    unittest.main()


