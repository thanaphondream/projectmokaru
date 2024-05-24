from rest_framework import generics
from .models import Register
from .serializers import RegisterSerializer

class RegisterUpdate1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = "pk"