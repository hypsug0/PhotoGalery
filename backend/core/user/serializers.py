# core/user/serializers.py
from core.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_active",
            "is_photographer",
            "avatar",
            "created",
            "updated",
        ]
        read_only_field = ["is_active", "created", "updated"]
