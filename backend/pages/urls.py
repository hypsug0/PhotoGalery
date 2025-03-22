from django.urls import path

from .views import (
    AlbumCreateView,
    AlbumUpdateView,
    AlbumView,
    Home,
    PhotoCreateView,
)

app_name = "pages"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("album", AlbumCreateView.as_view(), name="album-create"),
    path(
        "album/<slug:slug>/edit", AlbumUpdateView.as_view(), name="album-edit"
    ),
    path("album/<slug:slug>", AlbumView.as_view(), name="album"),
    path("photo", PhotoCreateView.as_view(), name="photo-create"),
]
