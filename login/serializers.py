from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    confirmpassword = serializers.CharField(write_only=True)

    class Meta:
        model = Register
        fields = ['name', 'email', 'password', 'confirmpassword']

    def validate(self, data):
        if data['password'] != data['confirmpassword']:
            raise serializers.ValidationError("Password and Confirm Password do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmpassword')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('confirmpassword')
        return super().update(instance, validated_data)