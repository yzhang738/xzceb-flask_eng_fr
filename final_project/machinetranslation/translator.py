"""
English to French translation using IBM Watson translator
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

def english_to_french(text):
    """
        English to French translation function
    """ 
    translated = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    return translated['translations'][0].get('translation')

def french_to_english(text):
    """
        French to English translation function
    """
    translated = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    return translated['translations'][0].get('translation')

def convert_dic_to_str(dict):
    """
        Since Watson translator returns translation results in python dictionaries,  
        we need to convert them to strings for comparision
    """
    # tran_list = dict['translations']
    translated_text = dict['translations'][0].get('translation')
    return translated_text
