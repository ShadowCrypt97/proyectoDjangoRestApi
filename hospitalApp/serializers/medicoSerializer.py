from re import M
from hospitalApp.models.medicos import Medico
from rest_framework import serializers

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['especialidad','fecha_registro']