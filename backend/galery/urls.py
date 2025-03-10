from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PhotoViewset, TagsViewset

app_name = "galery"

router = DefaultRouter()

router.register("photo", PhotoViewset, basename="photo_api")
router.register("tags", TagsViewset, basename="tags_api")

urlpatterns = [
    path("galery/", include(router.urls)),
]
