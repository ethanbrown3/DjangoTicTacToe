from django.conf.urls import url
from django.urls import path, re_path

from .views import home


urlpatterns = [
    path('home', home)
]