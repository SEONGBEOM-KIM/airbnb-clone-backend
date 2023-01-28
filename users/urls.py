from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me/", views.Me.as_view()),
    path("change_password/", views.ChangePassword.as_view()),
    path("log_in/", views.LogIn.as_view()),
    path("log_out/", views.LogOut.as_view()),
    path("token_login", obtain_auth_token),
    path("@<str:username>/", views.PublicUser.as_view()),
]
