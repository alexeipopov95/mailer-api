from rest_framework.serializers import ModelSerializer
from api.models.email import Email

__all__ = [
    "EmailSerializers",
]

class EmailSerializers(ModelSerializer):
    class Meta:
        model = Email
        fields = [
            "title",
            "subject",
            "email_body",
            "email_from",
            "email_to",
            "email_type",
        ]