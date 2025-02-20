
from django.core.mail import send_mail

from django.contrib.auth.models import User

from rest_framework import viewsets

from authorization.permissions import *
from .serializers import *
from .models import *
from assets.viewsets import *

import os


def notify_on_planning(event: Event):
    mail_message = (
        f"A new {event.title} event "
        f"has been planned by {event.organizer} "
        f"on {event.datetime.date()} "
        f"at {event.datetime.time()} "
        f"at {event.location} place! "
        f"{event.description}"
    )
    send_mail(
        'New Event',
        mail_message,
        os.getenv('EMAIL_HOST_USER'),
        [event.user.email]
    )

class EventViewSet(PrivateModelViewSetQuerySetGetter, viewsets.ModelViewSet):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = general_permission_classes

    def perform_create(self, serializer: EventSerializer):
        event = serializer.save()
        notify_on_planning(event)
