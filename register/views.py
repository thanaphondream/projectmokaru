from rest_framework import generics, status
from .models import Rg
from .serializers import RgSerializer, LoginSerializer1
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RgListCreate(generics.ListCreateAPIView):
    queryset = Rg.objects.all()
    serializer_class = RgSerializer

class LoginView1(generics.GenericAPIView):
    queryset = Rg.objects.all()
    serializer_class = LoginSerializer1

    def post(self, request, *args, **kwargs):
        emails = request.data.get('emails')
        passwords = request.data.get('passwords')
        try:
            user = Rg.objects.filter(emails=emails).first()
            print("User Password Hash:", user.passwords)
            print("Entered Password:", passwords)
            make = make_password(passwords)
            
            if check_password(passwords, user.passwords):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Rg.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)