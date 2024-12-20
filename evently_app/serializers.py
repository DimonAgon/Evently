
from rest_framework import serializers

from .models import *

import copy

from typing import Dict, Any


class EventSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    location = serializers.CharField()
    organizer = serializers.CharField()
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]) -> Event:
        user = self.context['request'].user
        validated_data_copy = copy.deepcopy(validated_data)
        location_name = validated_data['location']
        del validated_data_copy['location']
        location = Location.objects.get_or_create(name=location_name)[0]
        del validated_data_copy['organizer']
        organizer_name = validated_data['organizer']
        organizer = Organizer.objects.get_or_create(name=organizer_name)[0]
        new_event = Event(location=location, organizer=organizer, **validated_data_copy, user=user)
        new_event.save()
        return new_event