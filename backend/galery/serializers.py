import json

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Photo, Tags


class JSONSerializerField(serializers.Field):
    """Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return json.loads(value)


class TagsSerializer(ModelSerializer):

    class Meta:
        model = Tags
        fields = ("label",)


class PhotoSerializer(ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    exif_data = JSONSerializerField()

    class Meta:
        model = Photo
        fields = (
            "name",
            "description",
            "image",
            "exif_data",
            "photographer",
            "tags",
            "timestamp_create",
        )
