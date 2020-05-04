from rest_framework import serializers
from .models import linksData



class linksDataSerializer (serializers.ModelSerializer):

    class Meta:
        model = linksData
        fields = ['spmiProfileLink',
              'rsciID',
              'spinID',
              'scopusID',
              'researcherID',
              'orcidID',
              'rsciProfileLink',
              'scopusProfileLink',
              'publonsProfileLink',
              'orcidProfileLink',
              'researchProfileLink',
              'scholarProfileLink']



