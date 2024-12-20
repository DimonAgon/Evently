
from rest_framework import viewsets

from authorization.permissions import *
from .serializers import *
from .models import *
from assets.viewsets import *


class EventViewSet(PrivateModelViewSetQuerySetGetter, viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = general_permission_classes