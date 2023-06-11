from rest_framework import viewsets

from .models import Activity
from .serializers import ActivitySerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

