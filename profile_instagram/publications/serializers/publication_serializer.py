"""Publication serializer model."""

# Django REST framework
from rest_framework import serializers

# Models
from profile_instagram.publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta options."""
        model = Publication
        fields = '__all__'
