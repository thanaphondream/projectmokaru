from rest_framework import serializers
from .models import Register
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    confirmpassword = serializers.CharField(write_only=True)

    class Meta:
        model = Register
        fields = ['id', 'name', 'email', 'password', 'confirmpassword', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirmpassword']:
            raise serializers.ValidationError("Password and Confirm Password do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmpassword')
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('confirmpassword')
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['email', 'password']
        # extra_kwargs = {'password': {'write_only': True}}
        
class Rge(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['id', 'name', 'email', 'password', 'role']