"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from profile_instagram.utils.audit_model import AuditModel


class User(AuditModel, AbstractUser):
    """Users model.

    Extends from Django's AbstractUser, change the username field
    to email and add some extra fields."""

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_verified = models.BooleanField(
        'Verified',
        default=True,
        help_text='Set to true when the user have verified email address.'
    )

    profile = models.OneToOneField('users.Profile', on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
