import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['APIKEY']
url = os.environ['URL']

APIKEY1 = '..'
URL1 = '..'
VERSION = '2018-05-01'
GATEWAY='https://api.us-south.language-translator.watson.cloud.ibm.com'

authenticator = IAMAuthenticator(APIKEY1)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(GATEWAY)
#language_translator.set_disable_ssl_verification(True)

languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-de').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

def english_to_french(text1):
    """
    This function translates english to french
    """
    frenchtranslation = language_translator.translate(text=text1, model_id='en-fr').get_result()

    return frenchtranslation.get("translations")[0].get("translation")


def french_to_english(text1):
    """
    This function translates french to english
    """
    englishtranslation = language_translator.translate(text=text1, model_id='fr-en').get_result()

    return englishtranslation.get("translations")[0].get("translation")
