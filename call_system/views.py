from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import customSerializer

class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = customSerializer
