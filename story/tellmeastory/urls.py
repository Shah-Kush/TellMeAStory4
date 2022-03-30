from django.urls import path, include
from . import views

app_name = "tellmeastory"
urlpatterns = [
    path("", views.index, name="index"),
    path("account/<str:username>/", views.account, name="account_page"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("addtags/", include("managetags.urls"))
]
