from django.shortcuts import render

from gameplay.models import Game


def home(request):
    """
    Render player home page
    :param request:
    :return:
    """
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})
