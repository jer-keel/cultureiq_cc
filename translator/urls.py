from django.conf.urls import url

from . import views
from . import apis

app_name = 'translator'

urlpatterns = [
    url(r'^$', views.index, name="index"),  # /
    url(r'^texts/$', views.texts, name="texts"),  # /texts
    url(r'^translate/$', views.translate, name="translate"),  # /translate/
    url(r'^api/translate/$', apis.translate),
    url(r'^api/translations/$', apis.translations),
]
