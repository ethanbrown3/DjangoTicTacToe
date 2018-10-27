from django.shortcuts import render


def home(request):
    """
    Render player home page
    :param request:
    :return:
    """
    return render(request, "player/home.html")