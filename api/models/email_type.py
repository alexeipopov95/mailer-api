"""
Module where defining the EmailType model.
Here we define the diferent types for the email, for example;
- Notification type
- Alert Type
- Promotional Type
etc.
"""
from django.db import models
from commons.models import CommonProperties


class EmailType(CommonProperties):
    name = models.CharField(max_length=254)
    template = models.CharField(max_length=254, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"