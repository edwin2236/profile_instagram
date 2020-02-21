"""ConsolidatedFilesUploaded model serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from profile_instagram.publications.models import Publication

# Serializers
from profile_instagram.users.serializers import UserSerializer
from profile_instagram.publications.serializers import CommentSerializer


class PublicationsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    comments = CommentSerializer(many=True)

    class Meta:
        """Meta options."""
        model = Publication
        fields = ['description', 'numbers_likes', 'user', 'comments']
