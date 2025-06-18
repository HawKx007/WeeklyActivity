from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Game, Review, Tags, Developer
from rest_framework import generics, viewsets
from .serializers import GameSerializer, DeveloperSerializer


# HTML Views
class GameListView(generic.ListView):
    template_name = 'gamereview/gameList.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class ReviewListView(generic.DetailView):  # ✅ use DetailView for a single game
    model = Game
    template_name = 'gamereview/review.html'
    context_object_name = 'game'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def tag_list(request):  # ✅ Renders the tags page
    tags = Tags.objects.all()
    return render(request, 'gamereview/taglist.html', {'tags': tags})


# REST API Views
class GameApiView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
