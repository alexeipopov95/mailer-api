from django.urls import path, include
from rest_framework import routers
from api.views import EmailView

router = routers.DefaultRouter()
router.register("emails", EmailView)

urlpatterns = [
    path("mailer/", include(router.urls))
]
