from rest_framework import serializers
from .models import Alerta

class RegistroTemblorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'