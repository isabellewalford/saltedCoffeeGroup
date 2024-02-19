from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/signup/", views.signup_view, name="signup"),
    path("accounts/logout/", views.logout_view, name="logout"),

    path("accounts/user/", views.user_view, name="user"),
    path("accounts/user/photo", views.photo_view, name="photo"),
]
