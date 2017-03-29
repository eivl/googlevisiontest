# -*- coding: utf-8 -*-
from google.cloud import translate


def translate_text(text, target='en'):
    """
    Target must be an ISO 639-1 language code.
    https://cloud.google.com/translate/docs/languages
    """
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

example_text = '''Hola saludos desde Colombia excelentes tutoriales me gustaría poder por lo menos tener los subtitulos ene español ...excelente gracias por compartir tus conocimientos'''
translate_text(example_text.encode('utf-8'), target='en')
