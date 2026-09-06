from rest_framework import serializers
from .models import RegistroTemblor

class RegistroTemblorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroTemblor
        fields = '__all__'