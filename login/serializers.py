from rest_framework import serializers
from .models import Register
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    confirmpassword = serializers.CharField(write_only=True)

    class Meta:
        model = Register
        fields = ['id', 'name', 'email', 'password', 'confirmpassword', 'role']
        extra_kwargs = {'password': {'write_only': False}}  # แก้ไข write_only เป็น False เพื่อให้แสดงรหัสผ่านได้

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