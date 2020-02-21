"""Publication views."""

# Django REST framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Models
from profile_instagram.publications.models import Publication

# Serializer
from profile_instagram.publications.serializers import PublicationSerializer, PublicationReadSerializer


class PublicationList(APIView):
    def get(self, request, format=None):
        publications = Publication.objects.all()
        serializer = PublicationReadSerializer(publications, many=True)
        return Response(serializer.data)

    def post(self, resquest, format=None):
        serializer = PublicationSerializer(data=resquest.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
