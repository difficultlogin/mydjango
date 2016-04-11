from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<id>[0-9])/$', category),
    url(r'^(?P<id_category>[0-9])/(?P<id>[0-9])/$', post),
]