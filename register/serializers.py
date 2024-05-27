# from rest_framework import serializers
# from .models import Register
# from django.contrib.auth.models import User

# class RegisterSerializer(serializers.ModelSerializer):
#     # confirmpassword = serializers.CharField(write_only=True)

#     class Meta:
#         model = Register
#         fields = ['id','name', 'email', 'password', 'confirmpassword']
#         extra_kwargs = { 'password': {'write_only': True}
#         }

#         def create(self, validated_data):
#             password = validated_data.pop('password', None)
#             instance = self.Meta.model(**validated_data)
#             if password is not None:
#                 isinstance.set_password(password)
#             instance.save()
#             return instance
    

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class Bmm(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"