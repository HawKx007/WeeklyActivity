from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Game, Review, Tags  # Make sure Review and Tags are imported

class GameListView(generic.ListView):
    template_name = 'gamereview/gameList.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class ReviewListView(generic.DetailView):  # ✅ use DetailView instead of ListView
    model = Game
    template_name = 'gamereview/review.html'
    context_object_name = 'game'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def tag_list(request):  # ✅ Add this view to fix the tag_list error
    tags = Tags.objects.all()
    return render(request, 'gamereview/taglist.html', {'tags': tags})
