from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.serializers import EmailSerializers
from api.models.email import Email

__all__= [
    "EmailView",
]

class EmailView(ModelViewSet):
    http_method_names = ["get", "post"]
    lookup_field = "visible_id"
    queryset = Email.objects.all()
    serializer_class = EmailSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        # Aqui va a crear el mail para ser lanzado.
        # serializers.send_email()
        serializer.save()