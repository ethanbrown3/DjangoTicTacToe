from django.shortcuts import render

from gameplay.models import Game


def home(request):
    """
    Render player home page
    :param request:
    :return:
    """
    return render(request, "player/home.html",
                  {'ngames': Game.objects.count()})
