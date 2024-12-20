
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from assets.viewsets import *

from authorization.forms import *
from authorization.infrastructure.enums import *
from .serializers import *
from .permissions import *


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = NativeUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = NativeUserCreationForm()

    context = {
        'form': form,
        'authorization_type': AuthorizationType.REGISTRATION
    }
    return render(request, 'registration_window.html', context=context)


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = NativeAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = NativeAuthenticationForm()

    context = {
        'form': form,
        'authorization_type': AuthorizationType.LOGGING_IN
    }
    return render(request, 'logging_in_window.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login')


class TokenViewSetNative(PrivateModelViewSetQuerySetGetter, viewsets.ModelViewSet):
    model = Token
    queryset = Token.objects.all()
    serializer_class = TokenSerializerNative
    permission_classes = general_permission_classes


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = general_permission_classes
    http_method_names = ['get', 'put', 'update']

    def list(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)