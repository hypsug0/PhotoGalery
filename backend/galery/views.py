from rest_framework.viewsets import ModelViewSet

from .models import Photo, Tags
from .serializers import PhotoSerializer, TagsSerializer

# Create your views here.


class TagsViewset(ModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()


class PhotoViewset(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
