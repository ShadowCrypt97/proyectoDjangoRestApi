from rest_framework import serializers
from hospitalApp.models.medicos import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['especialidad','fecha_registro']
    