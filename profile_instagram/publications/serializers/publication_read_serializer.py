"""Publication serializer model."""

# Django REST framework
from rest_framework import serializers

# Models
from profile_instagram.publications.models import Publication

# Serializer
from profile_instagram.users.serializers import UserSerializer


class PublicationReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        """Meta options."""
        model = Publication
        fields = ['picture', 'description', 'numbers_likes', 'user']
