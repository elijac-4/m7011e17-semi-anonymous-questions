from .models import Text
from rest_framework import viewsets
from .serializers import TextSerializer


class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
