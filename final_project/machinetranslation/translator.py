"""
English to French translation using IBM Watson translator
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
        English to French translation function
    """ 
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    """
        French to English translation function
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text

def convert_dic_to_str(dict):
    """
        Since Watson translator returns translation results in python dictionaries, we need to convert them 
        to strings for comparision
    """
    tran_list = dict['translations']
    translated_text = tran_list[0].get('translation')
    return translated_text
