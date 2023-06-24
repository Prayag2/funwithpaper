from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('games/', views.GamesView.as_view(), name="games"),
    path('search/', views.search, name="search"),
    path('games/<int:game_id>/', views.game, name="game"),
    path('category/<str:category_name>/', views.category, name="category"),
    path('request/', views.request_game, name="request_game"),
    path('games/<int:pk>/download', views.download, name="download")
]
