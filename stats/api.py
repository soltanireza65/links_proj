from rest_framework import viewsets, permissions
from stats.models import Click
from stats.serializers import ClickSerializer


class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClickSerializer
