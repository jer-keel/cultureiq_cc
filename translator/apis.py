from django.shortcuts import get_list_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.core import serializers
from langdetect import detect
from googleapiclient.discovery import build

import json
import html
from .models import TranslatedText


def translate(request):
    return HttpResponse("Translate")


def translations(request):
    """Return a JSON object of all of the pervious translations

    Args:
        request (HttpRequest): The request object and it's parameters

    Returns:
        JsonResponse: A JSON encoded response of all translations
    """
    texts = get_list_or_404(TranslatedText.objects.order_by("-translate_date"))
    response_dict = {
        "translations": [],
    }

    # Formmat response
    for text in texts:
        json_obj = {
            "original_text": text.original_text,
            "translated_text": text.translated_text,
            "detected_language": text.detected_language,
            "translate_date": text.translate_date.isoformat(),
        }
        response_dict["translations"].append(json_obj)

    return JsonResponse(response_dict)
