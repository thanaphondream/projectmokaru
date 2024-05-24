from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import Register

class username(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class RegisterUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = "pk"