from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from .models import Register
from rest_framework.views import APIView
# from rest_framework.exceptions import AuthenticationFailed
# from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, Bmm
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class username(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = Bmm

class RegisterUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = "pk"

# class LoginView1(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = Register.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')
        
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')
        
#         return Response(user)

# class UserRegistration(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserLogin(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user is None:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }, status=status.HTTP_200_OK)

class RegisterView1(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user).data,
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)

class LoginView1(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        