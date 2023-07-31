from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class Registration(viewsets.ModelViewSet):

    queryset = CandidateInfo.objects.all()
    serializer_class = RegistrationSerializer


