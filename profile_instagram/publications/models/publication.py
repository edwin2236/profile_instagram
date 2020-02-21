"""Profile model."""

# Django
from django.db import models

# Utilities
from profile_instagram.utils.audit_model import AuditModel


class Publication(AuditModel):
    """Profile model."""

    picture = models.ImageField(
        upload_to='publications/pictures/',
        blank=True,
        null=True
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )

    numbers_likes = models.PositiveIntegerField(default=0)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
