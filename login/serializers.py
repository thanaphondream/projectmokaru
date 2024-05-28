from rest_framework import serializers
from register.models import Register

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['email', 'password']