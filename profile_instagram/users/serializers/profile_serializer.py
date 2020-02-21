"""Profile serializer."""

# Django
from rest_framework import serializers

# Models
from profile_instagram.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
