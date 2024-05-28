from rest_framework import serializers
from .models import Register
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ['id', 'name', 'email', 'password', 'confirmpassword', 'role']

class Rg(serializers.ModelSerializer):

    class Mega:
        model = Register
        fields = '__all__'