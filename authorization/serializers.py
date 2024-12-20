
from rest_framework import serializers

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from typing import Dict, Any


class TokenSerializerNative(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
        read_only_fields = ['key']

    def create(self, validated_data: Dict[str, Any]):
        user = self.context['request'].user
        token_query = Token.objects.filter(user=user)
        if token_query.exists():
            return token_query.first()
        token = Token.objects.create(user=user)
        token.save()
        return token

class UserSerializer(serializers.ModelSerializer):
    events = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = "__all__"