from django.utils.translation import get_language
from rest_framework.viewsets import ModelViewSet

from .models import Photo, Tags
from .serializers import PhotoSerializer, TagsSerializer

# Create your views here.


class TagsViewset(ModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()

    def get_queryset(self):
        lang = get_language()
        # Adjust the query based on the language, e.g., filtering or annotating
        return super().get_queryset().filter(language=lang)


class PhotoViewset(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
