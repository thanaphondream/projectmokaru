from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Register
from .serializers import RegisterSerializer
from django.contrib.auth.hashers import check_password

class RegisterView(generics.CreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Register.objects.get(email=email)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Register.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UserDetailView(generics.RetrieveAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = 'email'

class UsersGet(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer