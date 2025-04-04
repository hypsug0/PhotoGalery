# from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from galery.models import Album, Photo


class Home(ListView):
    template_name = "home.html"
    model = Album


class AlbumCreateView(CreateView):
    """Create album"""

    model = Album
    template_name = "form.html"
    fields = ["label", "description"]

    def get_success_url(self):
        return reverse("pages:album", kwargs={"slug": self.object.slug})


class AlbumUpdateView(UpdateView):
    """Create album"""

    model = Album
    template_name = "form.html"
    fields = ["label", "description"]

    def get_success_url(self):
        return reverse("pages:album", kwargs={"slug": self.object.slug})


class AlbumView(DetailView):
    """Album detail"""

    model = Album
    template_name = "album.html"


class PhotoCreateView(CreateView):
    """Create photo"""

    model = Photo
    template_name = "form.html"
    fields = [
        "album",
        "name",
        "description",
        "tags",
        "image",
        "geom",
        "city",
        "country",
    ]

    def get_success_url(self):
        return reverse("pages:album", kwargs={"slug": self.object.album.slug})

    def get_initial(self):
        initial = super().get_initial()
        if "slug" in self.kwargs:
            initial["album"] = Album.objects.get(slug=self.kwargs["slug"])
        return initial
