from rest_framework import serializers
from .models import personalData



class personalDataSerializer (serializers.ModelSerializer):

    class Meta:
        model = personalData
        fields = ('surname','name','link','academicDegree','position','department',)



