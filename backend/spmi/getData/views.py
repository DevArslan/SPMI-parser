from django.shortcuts import render
from rest_framework import viewsets
from .models import AuthorID
from .serializers import AuthorIDSerializer

class AuthorIDViewSet(viewsets.ModelViewSet):
    queryset = AuthorID.objects.all().order_by('scopusID')
    serializer_class = AuthorIDSerializer