from . import views
from django.urls import path

app_name = 'gamereviewapp'

urlpatterns = [
    path ('', views.gameListView.as_view(), name='gameList'),
    path ('<slug:slug>/', views.reviewListView.as_view(), name='review'),
]