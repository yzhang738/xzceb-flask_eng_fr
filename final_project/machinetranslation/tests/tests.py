import unittest
from  translator import english_to_french, french_to_english, convert_dic_to_str

class Test_english_to_french(unittest.TestCase): 
    def test1(self):
        message = "English and French translation are not equal!"
        # en_translation = english_to_french('I')
        # en_text = convert_dic_to_str(en_translation)
        #self.assertEqual(convert_dic_to_str(english_to_french('Blue')), 'bleu', message)
        self.assertEqual(convert_dic_to_str(english_to_french('Hello')), 'Bonjour', message)

class Test_french_to_english(unittest.TestCase): 
    def test1(self):
        message = "English and French translation are not equal!"
        self.assertEqual(convert_dic_to_str(french_to_english('Bonjour')), 'Hello', message)
 
unittest.main()