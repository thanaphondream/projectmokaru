from rest_framework import serializers
from .models import Rg
from django.contrib.auth.hashers import make_password

class RgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rg
        fields = ['id', 'names', 'emails', 'passwords', 'roles']


class LoginSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Rg
        fields = ['emails', 'passwords']