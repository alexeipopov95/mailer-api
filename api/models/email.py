"""
Here we are going to define the base for the Emails.
"""
from django.db import models
from api.models.email_type import EmailType
from commons.models import CommonProperties


class Email(CommonProperties):
    title = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    email_body = models.TextField(blank=True, null=True)
    email_from = models.EmailField(max_length=254, default="test@test.com")
    email_to = models.EmailField(max_length=254)
    email_type = models.ForeignKey(EmailType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"[{self.id}] -{self.title}"