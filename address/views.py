from django.shortcuts import render
from rest_framework import generics
from .serializers import AddressSerializer
from .models import Address

class address(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer