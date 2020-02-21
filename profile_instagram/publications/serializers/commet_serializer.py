"""Comment serializer model."""

# Django REST framework
from rest_framework import serializers

# Models
from profile_instagram.publications.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
