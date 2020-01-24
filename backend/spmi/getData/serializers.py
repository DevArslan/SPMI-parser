from rest_framework import serializers
from .models import AuthorID

class AuthorIDSerializer (serializers.ModelSerializer):

    class Meta:
        model = AuthorID
        fields = ('scopusID',)