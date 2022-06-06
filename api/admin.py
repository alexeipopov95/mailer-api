from django.contrib import admin
from api.models.email import Email
from api.models.email_type import EmailType

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subject",
        "email_body",
        "email_from",
        "email_to",
        "email_type",
    )


@admin.register(EmailType)
class EmailTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "template",
        "is_available",
    )