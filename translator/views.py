from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.utils.html import escape
from datetime import datetime
from langdetect import detect

from googleapiclient.discovery import build
import json
import html
from .models import TranslatedText

# Setup Google API token and build the Google translation service
API_TOKEN = json.load(open("translator/config/google_api.json"))["API_TOKEN"]
service = build("translate", "v2", developerKey=API_TOKEN)

# Parse language codes csv, create dictionary
lang_file = open("translator/language-codes.csv", "r")
lang_dict = {}
for line in lang_file:
    args = line.strip().replace("\"", "").split(",")
    lang_dict[args[0]] = args[1]


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
            input_string = escape(input_string)

            # If error occurs let the user know
            try:
                lang = detect(input_string)
            except:
                return JsonResponse({
                    "translated_text": "Could not detect language",
                    "detected_language": "Could not detect language"
                })

            print(lang)
            if lang != "en":
                translated_text = service.translations().list(
                    source=lang,
                    target="en",
                    q=[input_string]
                ).execute()["translations"][0]["translatedText"]
            else:
                translated_text = input_string

            # Store the information in the database
            text = TranslatedText()
            text.original_text = input_string
            text.translated_text = html.unescape(translated_text)
            text.detected_langugae_code = lang
            if lang in lang_dict:
                text.detected_language = lang_dict[lang]
            else:
                text.detected_language = lang
            text.save()

            json_response = {
                "translated_text": text.translated_text,
                "detected_language": text.detected_language,
            }
            return JsonResponse(json_response)
    else:
        return HttpResponseRedirect("/texts")
