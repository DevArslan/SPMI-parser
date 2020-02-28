from django.shortcuts import render
from rest_framework import viewsets
from .models import scopusData
from .serializers import scopusDataSerializer

class scopusDataViewSet(viewsets.ModelViewSet):
    queryset = scopusData.objects.all().order_by('author','creator','title','journal','date','volume','issue','pages','doi')
    serializer_class = scopusDataSerializer