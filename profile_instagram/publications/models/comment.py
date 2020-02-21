"""Profile model."""

# Django
from django.db import models

# Utilities
from profile_instagram.utils.audit_model import AuditModel


class Comment(AuditModel):
    """Profile model."""

    description = models.TextField(max_length=255)

    publication = models.ForeignKey("publications.Publication", on_delete=models.CASCADE)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
