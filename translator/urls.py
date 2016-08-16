from django.conf.urls import url

from . import views
from . import apis

app_name = 'translator'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^translations/$', views.index, name="translations"),
    url(r'^api/translate/$', apis.translate, name="api_translate"),
    url(r'^api/translations/$', apis.translations, name="api_translations"),
]
