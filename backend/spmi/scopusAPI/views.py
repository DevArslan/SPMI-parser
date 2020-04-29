from django.shortcuts import render
from rest_framework import viewsets
from .models import scopusData
from .serializers import scopusDataSerializer
from rest_framework import permissions
from rest_framework.authtoken.models import Token

class scopusDataViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated,]
    queryset = scopusData.objects.all().order_by('author','creator','title','journal','date','volume','issue','pages','doi')
    serializer_class = scopusDataSerializer