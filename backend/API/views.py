from django.shortcuts import render
from rest_framework import viewsets
from .serializers import APISerializer
from .models import API

# Create your views here.

class APIView(viewsets.ModelViewSet):
    serializer_class = APISerializer
    queryset = API.objects.all()