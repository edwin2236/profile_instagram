"""Profile model."""

# Django
from django.db import models

# Utilities
from profile_instagram.utils.audit_model import AuditModel


class Profile(AuditModel):
    """Profile model."""

    avatar = models.ImageField(
        'Profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    date_birth = models.DateField(auto_now=False, auto_now_add=False)

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )

    site_web = models.CharField(max_length=150)
