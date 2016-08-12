from django.conf.urls import url

from . import views

app_name = 'translator'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^texts/$', views.texts, name="texts"),
    url(r'^translate/$', views.translate, name="translate")
]
