import unittest
from  translator import english_to_french, french_to_english, convert_dic_to_str

class Test_english_to_french(unittest.TestCase): 
    def test1(self):
        message = "The translation are not equal!"
        self.assertEqual(english_to_french('Hello'), 'Bonjour', message)
        
class Test_french_to_english(unittest.TestCase): 
    def test3(self):
        message = "The translation are not equal!"
        self.assertEqual(french_to_english('Bonjour'), 'Hello', message)
    # def test4(self):
    #     message = "The translation are not equal!"
    #     self.assertNotEqual(convert_dic_to_str(french_to_english('Bleu')), 'Hello', message)

unittest.main()
