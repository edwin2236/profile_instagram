"""Publication views."""

# Django REST framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Models
from profile_instagram.publications.models import Comment

# Serializer
from profile_instagram.publications.serializers import CommentSerializer, CommentReadSerializer


class CommentList(APIView):
    def get(self, request, publication_id, format=None):
        comments = Comment.objects.all().filter(publication=publication_id)
        serializer = CommentReadSerializer(comments, many=True)
        return Response(serializer.data)


class CommentCreate(APIView):
    def post(self, resquest, format=None):
        serializer = CommentSerializer(data=resquest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
