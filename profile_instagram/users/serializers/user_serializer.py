""" User model serializer."""

# Django REST framework
from rest_framework import serializers

# Models
from profile_instagram.users.models import User, Profile

# Serializer
from profile_instagram.users.serializers import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    def create(self, data):
        profile = Profile.objects.create(**data['profile'])
        user = User.objects.create_user(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username=data['email'],
            email=data['email'],
            password=data['password'],
            is_verified=True,
            profile=profile
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'profile']
