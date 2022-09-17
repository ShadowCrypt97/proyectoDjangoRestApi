from rest_framework import serializers
from hospitalApp.models.personas import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id_persona','nombres','apellidos','genero','telefono']
    