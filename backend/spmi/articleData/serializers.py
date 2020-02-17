from rest_framework import serializers
from .models import articleData

class articleDataSerializer (serializers.ModelSerializer):

    class Meta:
        model = articleData
        fields = ('spmiProfileLink','rsciID','spinID','scopusID','researcherID','orcidID','rsciProfileLink','scopusProfileLink','publonsProfileLink','orcidProfileLink','researchProfileLink','scholarProfileLink',)

