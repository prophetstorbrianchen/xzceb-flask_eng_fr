import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    if english_text == "":
        french_text = ""
    else:
        french_dict = language_translator.translate(text=english_text, model_id='en-fr').get_result()
        # print(json.dumps(frenchDict, indent=2, ensure_ascii=False))
        french_text = french_dict["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    if french_text == "":
        english_text = ""
    else:
        english_dict = language_translator.translate(text=french_text, model_id='fr-en').get_result()
        # print(json.dumps(englishDict, indent=2, ensure_ascii=False))
        english_text = english_dict["translations"][0]["translation"]
    return english_text


if __name__=="__main__":
    french_to_english("Bonjour")
