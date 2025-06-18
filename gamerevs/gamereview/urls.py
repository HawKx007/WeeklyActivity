from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DeveloperViewSet

app_name = 'gamereviewapp'

# Setup router for Developer API
router = DefaultRouter()
router.register(r'developers', DeveloperViewSet, basename='developer')

urlpatterns = [
    path('', views.GameListView.as_view(), name='gameList'),
    path('tags/', views.tag_list, name='tag_list'),

    # API routes
    path('api/gameapi/', views.GameApiView.as_view(), name='game-api'),
    path('api/gameapi/<int:pk>/', views.GameDetailApiView.as_view(), name='game-detail-api'),
    path('api/', include(router.urls)),  # <- this enables /api/developers/

    # Keep slug-based path at the very bottom
    path('<slug:slug>/', views.ReviewListView.as_view(), name='review'),
]
