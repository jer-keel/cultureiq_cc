from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.utils.html import escape
from datetime import datetime
from langdetect import detect

from googleapiclient.discovery import build
import json

from .models import TranslatedText

# Setup Google API token and build the Google translation service
API_TOKEN = json.load(open("translator/config/google_api.json"))["API_TOKEN"]
service = build("translate", "v2", developerKey=API_TOKEN)

# Define our two main views, index and translation archive
def index(request):
    return render(request, "translator/index.html")


def texts(request):
    texts = get_list_or_404(TranslatedText.objects.order_by('-translate_date'))
    return render(request, "translator/texts.html", {"texts": texts})


# Translation view, upon POST detect, translate and store, otherwise redirect
# to archive
def translate(request):
    if request.method == "POST":
        input_string = request.POST.get("input_string")
        if input_string is None:
            return Http404("That's not allowed!")
        else:
            # Determine language and send to google translate to translate
            lang = detect(input_string)
            print(lang)
            translated_text = service.translations().list(
                source=lang,
                target="en",
                q=[input_string]
            ).execute()["translations"][0]["translatedText"]

            # Store the information in the database
            text = TranslatedText()
            text.original_text = input_string
            text.translated_text = translated_text
            text.detected_langugae_code = lang
            text.detected_language = lang  # TODO: Determine detected language
            text.save()

            json_response = {
                "translated_text": translated_text,
                "detected_language": lang,
            }
            return JsonResponse(json_response)
    else:
        return HttpResponseRedirect("/texts")
