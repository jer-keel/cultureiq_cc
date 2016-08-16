from django.db import models
import json

# Create your models here.


class TranslatedText(models.Model):
    """This object represents the original text and translated text and the
    language of origin. All translated text is in English

    Attributes:
        original_text (str): The original text in the language
        translated_text (str): The English translation of the original
        translate_date (date): The date and time the translation occured
        detected_langugae_code (str): The ISO 639-1 language code
        detected_language (str): The name of the language
    """
    original_text = models.TextField()
    translated_text = models.TextField()
    translate_date = models.DateTimeField('date translated', auto_now_add=True, blank=True)
    detected_langugae_code = models.CharField(max_length=10)
    detected_language = models.CharField(max_length=100)

    def __str__(self):
        return self.original_text

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
