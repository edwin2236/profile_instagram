"""Users URL Configuration"""

# Django
from django.urls import path

# Django REST framework
from rest_framework.urlpatterns import format_suffix_patterns

# Django REST framework Simple JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Views
from profile_instagram.users.views import (
    UserSignUpAPIView,
    UserDetail,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/sign_up/', UserSignUpAPIView.as_view()),
    path('api/user_detail/<int:pk>', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
