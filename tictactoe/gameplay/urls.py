from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView

from .views import game_detail

urlpatterns = [
    re_path(r'detail/(?P<id>\d+)/$',
            game_detail,
            name='gameplay_detail')
]

