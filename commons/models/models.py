import uuid
from django.db import models

__all__ = [
    "CommonProperties"
]

class CommonProperties(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible_id = models.UUIDField(default=uuid.uuid4())