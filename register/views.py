from rest_framework import generics
from .models import Register
from .serializers import RegisterSerializer

class RegisterListCreate(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class Rgall(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
