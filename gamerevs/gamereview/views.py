from pyclbr import Class

from django.shortcuts import render
from django.views import generic
from .models import Game


# Create your views here.
class GameListView(generic.ListView):
    template_name = 'gamereview/gameList.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()

class ReviewListView(generic.ListView):
    model = Game
    template_name = 'gamereview/review.html'