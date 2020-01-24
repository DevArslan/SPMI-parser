from django.shortcuts import render
from rest_framework import viewsets
from .models import personalData
from .serializers import personalDataSerializer

class personalDataViewSet(viewsets.ModelViewSet):
    queryset = personalData.objects.all().order_by('surname','name','link','academicDegree','position','department')
    serializer_class = personalDataSerializer