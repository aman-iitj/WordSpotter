from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^(?P<word_id>\d+)/$', views.show_words)
    # url(r'^(?P<word_id>\d+)/$', views.show_words)
]