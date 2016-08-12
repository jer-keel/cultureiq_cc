from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.utils.html import escape
from langdetect import detect

from .models import TranslatedText


def index(request):
    return render(request, "translator/index.html")


def texts(request):
    texts = get_list_or_404(TranslatedText)
    return render(request, "translator/texts.html", {"texts": texts})


def translate(request):
    if request.method == "POST":
        input_string = request.POST.get("input_string")
        if input_string is None:
            return Http404("That's not allowed!")
        else:
            input_string = escape(input_string)
            lang = detect(input_string)
            return HttpResponse(lang)
    else:
        return HttpResponseRedirect("/texts")
