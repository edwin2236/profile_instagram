"""User view."""

# Django
from django.shortcuts import get_object_or_404

# Django REST framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Serializers
from profile_instagram.users.serializers import UserSerializer

# Models
from profile_instagram.users.models import User


class UserSignUpAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, model, pk):
        return get_object_or_404(model, pk=pk)

    def get(self, requet, pk, format=None):
        user = self.get_object(User, pk=pk)
        seriliazer = UserSerializer(user)
        return Response(seriliazer.data, status=status.HTTP_200_OK)
