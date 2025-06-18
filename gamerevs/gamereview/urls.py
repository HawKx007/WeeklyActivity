from django.urls import path
from . import views

app_name = 'gamereviewapp'

urlpatterns = [
    path('', views.GameListView.as_view(), name='gameList'),
    path('tags/', views.tag_list, name='tag_list'),# ✅ Capital G
    path('<slug:slug>/', views.ReviewListView.as_view(), name='review'),
    # ✅ Capital R
]
