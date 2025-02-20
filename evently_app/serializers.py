
from rest_framework import serializers

from .models import *

from typing import Dict, Any


class GetOrCreateSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data: str):
        return self.get_queryset().get_or_create(**{self.slug_field: data})[0]

class EventSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    title = serializers.CharField(style={'placeholder': 'title'})
    description = serializers.CharField(style={'placeholder': 'description'})
    location = GetOrCreateSlugRelatedField(
        slug_field='name',
        queryset=Location.objects.all(),
        style={
            'base_template': 'input.html',
            'placeholder': 'location'
        }
    )
    organizer = GetOrCreateSlugRelatedField(
        slug_field='name',
        queryset=Organizer.objects.all(),
        style={
            'base_template': 'input.html',
            'placeholder': 'organizer'
        }
    )
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]) -> Event:
        user = self.context['request'].user
        new_event = Event(**validated_data, user=user)
        new_event.save()
        return new_event