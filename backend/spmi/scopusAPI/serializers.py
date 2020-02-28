from rest_framework import serializers
from .models import scopusData

class scopusDataSerializer (serializers.ModelSerializer):

    class Meta:
        model = scopusData
        fields = ('author','creator','title','journal','date','volume','issue','pages','doi',)
