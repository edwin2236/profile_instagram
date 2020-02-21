"""Comment serializer model."""

# Django REST framework
from rest_framework import serializers

# Models
from profile_instagram.publications.models import Comment

# Serializers
from profile_instagram.users.serializers import UserSerializer


class CommentReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['description', 'publication', 'user']
