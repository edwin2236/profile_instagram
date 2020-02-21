"""Users URL Configuration"""

# Django
from django.urls import path

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from profile_instagram.publications.views import (
    PublicationList,
    CommentList,
    CommentCreate,
)

urlpatterns = [
    path('api/publications/', PublicationList.as_view(), name='publication'),
    path('api/comments/<int:publication_id>', CommentList.as_view(), name='comments'),
    path('api/comments/', CommentCreate.as_view(), name='comment_create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
