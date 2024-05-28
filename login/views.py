from rest_framework import generics, status
from register.models import Register
from .serializers import  LoginSerializer
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(generics.GenericAPIView):
    queryset = Register.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Register.objects.filter(email=email).first()
            print("User Password Hash:", user.password)
            print("Entered Password:", password)
            make = make_password(password)
            
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Register.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)