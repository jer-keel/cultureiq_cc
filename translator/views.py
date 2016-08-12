from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import TranslatedText
# Create your views here.


def index(request):
    return render(request, 'translator/index.html')


def texts(request):
    texts = get_list_or_404(TranslatedText)
    return render(request, 'translator/texts.html', {'texts': texts})
