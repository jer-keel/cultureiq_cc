from django.db import models

# Create your models here.


class TranslatedText(models.Model):
    original_text = models.TextField()
    translated_text = models.TextField()
    translate_date = models.DateTimeField('date translated')
    detected_langugae_code = models.CharField(max_length=10)
    detected_language = models.CharField(max_length=100)

    def __str__(self):
        return self.original_text
