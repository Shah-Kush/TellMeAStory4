from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "tellmeastory"
urlpatterns = [
    path("", views.register, name="register"),
    path("index/", views.index, name="index"),
    path("account/<str:username>/", views.account, name="account_page"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("map/" , views.map , name="map") ,
    path("addtags/", include("managetags.urls")),

    #edit post view
    path('modify/<post_id>', views.editPost, name="updatePost"),

    #delete post view (just deletes and redirects not an actual page)
    path('delete/<post_id>', views.deletePost, name="deletePost"),

    #standard django admin path
    path('admin/', admin.site.urls),
]
