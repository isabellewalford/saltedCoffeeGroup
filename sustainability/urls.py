from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("user/", views.user, name="user"),
    path("user/photo/", views.photo, name="photo"),
    path("user/collection/", views.collection, name="collection"),
]
