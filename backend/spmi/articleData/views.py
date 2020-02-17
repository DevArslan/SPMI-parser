from django.shortcuts import render
from rest_framework import viewsets
from .models import articleData
from .serializers import articleDataSerializer

class articleDataViewSet(viewsets.ModelViewSet):
    queryset = articleData.objects.all().order_by('spmiProfileLink','rsciID','spinID','scopusID','researcherID','orcidID','rsciProfileLink','scopusProfileLink','publonsProfileLink','orcidProfileLink','researchProfileLink','scholarProfileLink')
    serializer_class = articleDataSerializer